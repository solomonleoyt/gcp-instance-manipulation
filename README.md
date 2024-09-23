Note: this repo is not yet completed, it's under development
# gcp-instance-manipulation

### Purpose of the repository
To understand how can we interact with GCP compute engine services from github using github actions

### Pre-requisites
Create a BigQuery table (you can use this sample SQL code to create one): 
```sql
-- Create the table
CREATE TABLE `your_project.your_dataset.run_table_new` (
  customer_name STRING,
  customer_id INT64,
  sell_score FLOAT64
);

-- Insert the data
INSERT INTO `your_project.your_dataset.run_table_new` (customer_name, customer_id, sell_score)
VALUES
  ('Bob', 2, 90.2),
  ('Alice', 1, 85.5),
  ('Charlie', 3, 78.9),
  ('Diana', 4, 88.1),
  ('Eve', 5, 92.3);
```
Replace "your_project" with your GCP Project ID, and "your_dataset" with your BigQuery dataset ID. 
