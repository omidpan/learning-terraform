output "admin_access_role_arn" {
  value = data.aws_iam_role.admin_access.arn
}

output "credit_history_table" {
  value = aws_glue_catalog_table.credit_history_table.name
}

output "zipcode_features_table" {
  value = aws_glue_catalog_table.zipcode_features_table.name
}

output "redshift_cluster_identifier" {
  value = aws_redshift_cluster.feast_redshift_cluster.cluster_identifier
}