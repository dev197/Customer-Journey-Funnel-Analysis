Customer Journey & Funnel Analysis — Power BI

A Power BI project analyzing customer sessions, engagement, conversion, acquisition quality, customer drop-off, product performance, customer segments, and at-risk opportunity value.

This project was created using Microsoft Power BI only. It does not use React, JavaScript, a web application, or a database-backed dashboard.

Project objective

The goal of this analysis is to understand how users move through the customer journey and identify where potential customers leave before submitting a lead form.

The report focuses on the following business questions:
How much traffic and how many users are entering the journey?
How deeply are users engaging with the product experience?
Where are customers dropping out of the funnel?
Which acquisition sources bring higher-quality traffic?
Which products and customer segments represent the largest opportunity?
What actions could improve conversion and reduce opportunity loss?

Tools used

• Microsoft Power BI Desktop

• Pandas & Numpy

• Python

• SQL

Source file: cleaned_sessions.csv

Dataset overview

The dataset contains 5,000 customer sessions recorded between January and June 2025.

The analysis includes session information, user information, acquisition source, device, region, age band, income band, product, funnel stage, exit page, exit reason, and estimated opportunity value.

The dataset contains 2,629 unique users. Because there are 5,000 sessions, some users visited more than once. The average number of sessions per user is 1.90.

Power BI report pages

Page 1 — Executive Overview
<img width="795" height="509" alt="overview analysis" src="https://github.com/user-attachments/assets/06934866-e78b-4bad-a18b-a5af61f3cc6c" />


The Executive Overview page provides a high-level summary of the customer journey and business performance.

The page contains KPI cards for:

•
Total sessions

•
Unique users

•
Lead submissions

•
Form-submission conversion rate

•
Estimated at-risk opportunity

•
Average session duration

•
Average page views per session

The page also includes a monthly trend chart showing sessions and submitted leads over time. This helps compare traffic movement with conversion movement.

The main funnel visual shows that 92.5% of sessions reach a product page, but only 15.6% finally submit a lead form. This indicates that the main issue is not only traffic generation. The larger opportunity is improving the journey between engagement and conversion.

The most important executive findings are:

•
The dataset contains 5,000 sessions and 779 submitted leads.

•
Product-page reach is strong at 92.5%.

•
Calculator usage falls to 47.0% of sessions.

•
Final form submission is 15.6% of sessions.

•
Estimated at-risk opportunity is 218.6M in the source data's value units.

•
Mobile receives the most sessions but converts below Desktop.

•
Technical issues and unclear product value are major friction themes.

Page 2 — Customer Journey & Funnel Analysis
<img width="790" height="504" alt="Journey analysis" src="https://github.com/user-attachments/assets/62b83ccc-4e47-44c2-b52b-750f468e2fe4" />


This page focuses on how users progress through each stage of the customer journey.

The funnel stages are:

•
Website visit: 5,000 sessions

•
Product page viewed: 4,627 sessions

•
Calculator used: 2,348 sessions

•
CTA clicked: 1,502 sessions

•
Form started: 1,183 sessions

•
Form submitted: 779 sessions

The largest early-stage drop occurs between Product Page Viewed and Calculator Used. Only approximately 50.7% of product-page visitors continue to the calculator.

The next important issue occurs after users start the form. Approximately 65.8% of form starters submit the form, which means 34.2% abandon at the final stage.

This page also analyzes the reasons why users leave. The main exit reasons are:

•
Technical issue

•
Comparing alternatives

•
Unclear product value

•
High interest-rate concern

•
Calculator result not attractive

•
Required information unavailable

•
Too many required fields

•
Document requirement concern

The four largest exit reasons represent approximately 68.5% of non-submitters. This makes them the most important areas for product, marketing, and operations teams to investigate.

Page 3 — Acquisition & Marketing Performance
<img width="784" height="453" alt="Acquistion quality" src="https://github.com/user-attachments/assets/8f5daf6e-b284-42fc-bdec-12f6ff96e059" />
This page compares acquisition sources by session volume and form-submission conversion rate.

Organic Search brings the largest number of sessions, followed by Direct traffic and Paid Ads. However, the highest traffic source is not automatically the highest-quality source.

Referral is the best-performing source with an approximately 22.7% form-submission rate. Email follows at approximately 20.5%.

Organic Search converts at approximately 16.6%, while Direct converts at approximately 15.3%.

Paid Ads converts at approximately 10.7%, and Social Media is the weakest source at approximately 7.5%.

This means Referral converts approximately three times better than Social Media. Marketing performance should therefore be evaluated using lead conversion and lead quality, not only impressions, clicks, or sessions.

The page also includes source and device analysis. A particularly important pattern is the low Social Media mobile conversion rate of approximately 4.4%. This suggests that the campaign message, landing page, mobile experience, or audience targeting should be reviewed.

Page 4 — Product, Customer & Opportunity Analysis
<img width="792" height="465" alt="Product   Oppurtunity" src="https://github.com/user-attachments/assets/e0a8090e-d861-4279-bf51-cc2b7defe7f9" />
This page identifies which products and customer segments deserve the most attention.

Product analysis

Personal Loan is the primary opportunity engine in the dataset. It has the largest number of sessions, the highest product-level conversion rate, and the largest estimated opportunity value.

Personal Loan has approximately 1,739 sessions, a conversion rate of 17.2%, and 163.7M of estimated at-risk opportunity.

Credit Card has approximately 1,542 sessions, a conversion rate of 14.7%, and 37.0M of estimated at-risk opportunity.

Savings Account has approximately 1,007 sessions, a conversion rate of 16.2%, and 13.2M of estimated at-risk opportunity.

Insurance Plan has approximately 712 sessions, a conversion rate of 12.8%, and 4.7M of estimated at-risk opportunity.

Personal Loan should receive a dedicated optimization plan because improvements in this product journey could affect the largest opportunity pool.

Income-band analysis

Income is one of the strongest segmentation variables in the dataset.

The 100K+ income segment has an approximately 19.9% conversion rate.

The 50K–100K segment converts at approximately 17.3%.

The 25K–50K segment converts at approximately 14.6%.

The Below 25K segment converts at approximately 10.8%.

The 100K+ segment converts nearly twice as well as the Below 25K segment. Possible explanations include differences in affordability, eligibility, trust, product fit, and interest-rate sensitivity.

Age-band analysis

Age differences are smaller than income differences.

The 45–54 group has the highest age-band conversion at approximately 16.7%.

The 35–44 group converts at approximately 16.3%.

The 55+ group converts at approximately 15.3%.

The 25–34 group converts at approximately 14.9%.

The 18–24 group converts at approximately 14.4%.

Age can be used as a supporting segmentation variable, but income appears to be more important for explaining conversion differences.

New and returning user analysis

Returning users use the calculator and click the CTA slightly more often than new users. However, their final conversion rate is almost identical.

New users have approximately 46.2% calculator usage and a 15.7% form-submission rate.

Returning users have approximately 49.1% calculator usage and a 15.3% form-submission rate.

This suggests that returning users engage more deeply but still face similar late-stage form friction.
Business recommendations

1.
Improve the Product Page to Calculator transition with clearer value messaging and stronger calls to action.

2.
Investigate technical issues by separating page-load errors, validation errors, API failures, timeouts, and user abandonment.

3.
Optimize mobile landing pages and lead forms.

4.
Review Paid Ads and Social Media campaigns by campaign, audience, landing page, and downstream lead quality.

5.
Improve transparency around interest rates, eligibility, product benefits, and calculator results.

6.
Create a dedicated Personal Loan optimization workstream.

7.
Use Referral and Email as benchmarks for high-quality acquisition.

8.
Create clearer affordability and eligibility messaging for lower-converting income segments.

9.
Validate the business meaning of estimated opportunity value before using it as revenue or ROI.


