with base as (
    select
        campaign_name,
        clicks,
        impressions,
        clicks / nullif(impressions, 0) as ctr,
        date
    from {{ ref('google_ads') }}
)
select * from base;
