import random
import mlflow

mlflow.start_run()

accuracy = random.uniform(0.7, 0.95)

mlflow.log_metric("accuracy", accuracy)

run_id = mlflow.active_run().info.run_id

with open("accuracy.txt", "w") as f:
    f.write(str(accuracy))

with open("model_info.txt", "w") as f:
    f.write(run_id)

print("Accuracy:", accuracy)
print("Run ID:", run_id)

mlflow.end_run()
