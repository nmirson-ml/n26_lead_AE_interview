resource "confluent_connector" "bigquery_sink" {
  name     = "bigquery-sink-connector"
  config   = {
    "connector.class"                = "com.wepay.kafka.connect.bigquery.BigQuerySinkConnector"
    "tasks.max"                      = "1"
    "topics"                         = "facebook_ads_topic,google_ads_topic"
    "project.id"                     = var.gcp_project_id
    "datasets"                       = "${var.gcp_project_id}:marketing_data"
    "auto.create.tables"             = "true"
    "key.converter"                  = "org.apache.kafka.connect.storage.StringConverter"
    "value.converter"                = "org.apache.kafka.connect.json.JsonConverter"
    "value.converter.schemas.enable" = "false"
    "batch.size"                     = "1000"
    "bigquery.credentials.path"      = var.google_credentials_path
  }
  environment {
    cluster = confluent_kafka_cluster.basic.id
  }
}
