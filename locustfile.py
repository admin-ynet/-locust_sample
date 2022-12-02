from locust import HttpUser, task, constant_throughput


class HelloLocust(HttpUser):
    host = "http://localhost:10101/test"
    wait_time = constant_throughput(1)

    def on_start(self):
        pass
        # ターミナルID作成
        # SoriIF作成

    @task(1)
    def hello_locust1(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("statusCode is not 200")

    # @task(2)
    # def hello_locust2(self):
    #     with self.client.get("/", catch_response=True) as response:
    #         if response.status_code != 200:
    #             response.failure("statusCode is not 200")