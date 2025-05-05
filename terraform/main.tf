provider "snowflake" {
  alias      = "snowflake"
  account    = var.snowflake_account
  username   = var.snowflake_username
  password   = var.snowflake_password
  role       = var.snowflake_role
  region     = var.snowflake_region
}

resource "snowflake_database" "example" {
  name = "EXAMPLE_DB"
}
