import dagshub
dagshub.init(repo_owner='mail2singhumesh', repo_name='mlflow_tracking', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)