CREATE TABLE sessions (
    session_id                    VARCHAR(20)   PRIMARY KEY,
    user_id                       VARCHAR(20)   NOT NULL,
    session_start                 DATETIME2     NOT NULL,
    session_date                  DATE          NOT NULL,
    source                        VARCHAR(50)   NOT NULL,
    device                        VARCHAR(20)   NOT NULL,
    region                        VARCHAR(20)   NOT NULL,
    age_band                      VARCHAR(20)   NOT NULL,
    income_band                   VARCHAR(20)   NOT NULL,
    product                       VARCHAR(50)   NOT NULL,
    is_returning_user             BIT           NOT NULL,
    page_views                    INT           NOT NULL,
    session_duration_seconds      INT           NOT NULL,
    completed_stage                VARCHAR(50)  NOT NULL,
    product_page_viewed           BIT           NOT NULL,
    calculator_used                BIT          NOT NULL,
    cta_clicked                    BIT          NOT NULL,
    form_started                   BIT          NOT NULL,
    form_submitted                 BIT          NOT NULL,
    exit_page                      VARCHAR(100) NULL,
    exit_reason                    VARCHAR(100) NULL,
    estimated_opportunity_value    INT          NULL,
    session_month                  TINYINT      NOT NULL,
    session_week                   TINYINT      NOT NULL
);

CREATE INDEX idx_sessions_source  ON sessions(source);
CREATE INDEX idx_sessions_device  ON sessions(device);
CREATE INDEX idx_sessions_product ON sessions(product);
CREATE INDEX idx_sessions_form_submitted ON sessions(form_submitted);