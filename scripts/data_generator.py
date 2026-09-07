
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd


FUNNEL_STAGES = [
    "Website Visit",
    "Product Page Viewed",
    "Calculator Used",
    "CTA Clicked",
    "Lead Form Started",
    "Lead Form Submitted",
]

CHANNELS = ["Organic Search", "Paid Ads", "Direct", "Referral", "Email", "Social Media"]
CHANNEL_WEIGHTS = [0.25, 0.20, 0.20, 0.12, 0.13, 0.10]

DEVICES = ["Mobile", "Desktop", "Tablet"]
DEVICE_WEIGHTS = [0.58, 0.35, 0.07]

REGIONS = ["North", "South", "East", "West", "Central"]
REGION_WEIGHTS = [0.22, 0.20, 0.18, 0.24, 0.16]

PRODUCTS = [
    "Personal Loan",
    "Credit Card",
    "Savings Account",
    "Insurance Plan",
]
PRODUCT_WEIGHTS = [0.35, 0.30, 0.20, 0.15]

AGE_BANDS = ["18-24", "25-34", "35-44", "45-54", "55+"]
AGE_WEIGHTS = [0.12, 0.34, 0.28, 0.18, 0.08]

INCOME_BANDS = ["Below 25K", "25K-50K", "50K-100K", "100K+"]
INCOME_WEIGHTS = [0.18, 0.36, 0.32, 0.14]

EXIT_REASONS = {
    "Website Visit": [
        "Immediate bounce",
        "Landing page mismatch",
        "Slow page load",
        "Not ready to explore",
    ],
    "Product Page Viewed": [
        "Unclear product value",
        "High interest-rate concern",
        "Comparing alternatives",
        "Technical issue",
    ],
    "Calculator Used": [
        "Calculator result not attractive",
        "Required information unavailable",
        "Comparing alternatives",
        "Technical issue",
    ],
    "CTA Clicked": [
        "Form looked too long",
        "Privacy concern",
        "Not ready to apply",
        "Technical issue",
    ],
    "Lead Form Started": [
        "Too many required fields",
        "Document requirement concern",
        "Session timeout",
        "Technical issue",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate synthetic FinFlow website funnel data.")
    parser.add_argument("--sessions", type=int, default=5000, help="Number of website sessions to generate.")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducible output.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("data/raw"),
        help="Output directory for generated CSV files.",
    )
    return parser.parse_args()


def choose(rng: np.random.Generator, values: List[str], probabilities: List[float]) -> str:
    return str(rng.choice(values, p=probabilities))


def bounded_probability(value: float) -> float:
    return float(np.clip(value, 0.02, 0.98))


def stage_probabilities(channel: str, device: str, product: str, income_band: str) -> List[float]:
    """Return conditional probabilities for the five transitions after a visit."""
    channel_effect = {
        "Referral": 0.10,
        "Email": 0.06,
        "Direct": 0.04,
        "Organic Search": 0.02,
        "Paid Ads": -0.03,
        "Social Media": -0.06,
    }[channel]
    device_effect = {"Desktop": 0.06, "Mobile": 0.00, "Tablet": -0.02}[device]
    product_effect = {
        "Personal Loan": 0.04,
        "Credit Card": 0.03,
        "Savings Account": 0.01,
        "Insurance Plan": -0.02,
    }[product]
    income_effect = {"100K+": 0.06, "50K-100K": 0.03, "25K-50K": 0.00, "Below 25K": -0.04}[income_band]

    base = channel_effect + device_effect + product_effect + income_effect
    return [
        bounded_probability(0.91 + base * 0.25),  # Visit -> product page
        bounded_probability(0.42 + base),         # Product page -> calculator
        bounded_probability(0.58 + base * 0.80),  # Calculator -> CTA
        bounded_probability(0.72 + base * 0.70),  # CTA -> form start
        bounded_probability(0.56 + base * 0.90),  # Form start -> submit
    ]


def choose_exit_reason(rng: np.random.Generator, stage: str) -> str:
    reasons = EXIT_REASONS[stage]
    return str(rng.choice(reasons))


def build_session(
    session_number: int,
    start_date: pd.Timestamp,
    rng: np.random.Generator,
) -> Tuple[Dict[str, object], List[Dict[str, object]]]:
    session_id = f"S{session_number:06d}"
    user_id = f"U{rng.integers(1, max(2_000, session_number + 1)):06d}"
    session_date = start_date + pd.to_timedelta(int(rng.integers(0, 180)), unit="D")
    session_start = session_date + pd.to_timedelta(int(rng.integers(0, 86_400)), unit="s")

    channel = choose(rng, CHANNELS, CHANNEL_WEIGHTS)
    device = choose(rng, DEVICES, DEVICE_WEIGHTS)
    region = choose(rng, REGIONS, REGION_WEIGHTS)
    product = choose(rng, PRODUCTS, PRODUCT_WEIGHTS)
    age_band = choose(rng, AGE_BANDS, AGE_WEIGHTS)
    income_band = choose(rng, INCOME_BANDS, INCOME_WEIGHTS)
    is_returning_user = int(rng.random() < 0.27)

    page_views = int(rng.integers(1, 13))
    session_duration_seconds = int(rng.integers(15, 1_201))
    probabilities = stage_probabilities(channel, device, product, income_band)

    reached = [True]
    for probability in probabilities:
        reached.append(bool(rng.random() < probability and reached[-1]))

    completed_stage_index = max(i for i, did_reach in enumerate(reached) if did_reach)
    completed_stage = FUNNEL_STAGES[completed_stage_index]
    converted = int(completed_stage_index == len(FUNNEL_STAGES) - 1)

    exit_page = None if converted else completed_stage
    exit_reason = None if converted else choose_exit_reason(rng, completed_stage)
    lead_value = {
        "Personal Loan": 180_000,
        "Credit Card": 45_000,
        "Savings Account": 25_000,
        "Insurance Plan": 12_000,
    }[product]
    estimated_opportunity = 0 if converted else int(lead_value * rng.uniform(0.35, 0.90))

    session = {
        "session_id": session_id,
        "user_id": user_id,
        "session_start": session_start,
        "session_date": session_start.date(),
        "source": channel,
        "device": device,
        "region": region,
        "age_band": age_band,
        "income_band": income_band,
        "product": product,
        "is_returning_user": is_returning_user,
        "page_views": page_views,
        "session_duration_seconds": session_duration_seconds,
        "completed_stage": completed_stage,
        "product_page_viewed": int(reached[1]),
        "calculator_used": int(reached[2]),
        "cta_clicked": int(reached[3]),
        "form_started": int(reached[4]),
        "form_submitted": converted,
        "exit_page": exit_page,
        "exit_reason": exit_reason,
        "estimated_opportunity_value": estimated_opportunity,
    }

    events: List[Dict[str, object]] = []
    event_time = session_start
    for stage_index, did_reach in enumerate(reached):
        if not did_reach:
            break
        if stage_index > 0:
            event_time += pd.to_timedelta(int(rng.integers(20, 1_800)), unit="s")
        events.append(
            {
                "event_id": f"E{session_number:06d}{stage_index + 1:02d}",
                "session_id": session_id,
                "user_id": user_id,
                "event_timestamp": event_time,
                "stage_name": FUNNEL_STAGES[stage_index],
                "event_status": "Completed",
                "source": channel,
                "device": device,
                "region": region,
                "product": product,
            }
        )

    if not converted:
        failed_stage = FUNNEL_STAGES[completed_stage_index]
        events.append(
            {
                "event_id": f"E{session_number:06d}XX",
                "session_id": session_id,
                "user_id": user_id,
                "event_timestamp": event_time,
                "stage_name": failed_stage,
                "event_status": "Dropped Off",
                "source": channel,
                "device": device,
                "region": region,
                "product": product,
            }
        )

    return session, events


def generate_dataset(number_of_sessions: int, seed: int) -> Tuple[pd.DataFrame, pd.DataFrame]:
    rng = np.random.default_rng(seed)
    start_date = pd.Timestamp("2025-01-01")
    sessions: List[Dict[str, object]] = []
    events: List[Dict[str, object]] = []

    for session_number in range(1, number_of_sessions + 1):
        session, session_events = build_session(session_number, start_date, rng)
        sessions.append(session)
        events.extend(session_events)

    session_df = pd.DataFrame(sessions)
    event_df = pd.DataFrame(events)
    session_df["session_start"] = pd.to_datetime(session_df["session_start"])
    event_df["event_timestamp"] = pd.to_datetime(event_df["event_timestamp"])
    return session_df, event_df


def print_summary(session_df: pd.DataFrame, event_df: pd.DataFrame) -> None:
    total = len(session_df)
    submitted = int(session_df["form_submitted"].sum())
    print("FinFlow synthetic dataset generated")
    print(f"Sessions: {total:,}")
    print(f"Events: {len(event_df):,}")
    print(f"Form submissions: {submitted:,}")
    print(f"Overall conversion rate: {submitted / total * 100:.2f}%")
    print("\nCompleted stage counts:")
    print(session_df["completed_stage"].value_counts().reindex(FUNNEL_STAGES, fill_value=0).to_string())
    print("\nConversion by source:")
    source_summary = session_df.groupby("source")["form_submitted"].agg(["count", "sum"])
    source_summary["conversion_rate_pct"] = source_summary["sum"] / source_summary["count"] * 100
    print(source_summary.round(2).to_string())


def main() -> None:
    args = parse_args()
    if args.sessions < 100:
        raise ValueError("Use at least 100 sessions for meaningful segment analysis.")

    output_dir = args.output
    output_dir.mkdir(parents=True, exist_ok=True)

    sessions, events = generate_dataset(args.sessions, args.seed)
    sessions_path = output_dir / "finflow_sessions.csv"
    events_path = output_dir / "finflow_events.csv"
    sessions.to_csv(sessions_path, index=False)
    events.to_csv(events_path, index=False)

    print_summary(sessions, events)
    print(f"\nSaved sessions to: {sessions_path}")
    print(f"Saved events to:   {events_path}")


if __name__ == "__main__":
    main()