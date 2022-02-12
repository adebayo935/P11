from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def index(self):
        self.client.get("")

    @task
    def summary(self):
        self.client.post("/showSummary", {'email':'john@simplylift.co'})

    
    @task
    def book(self):
        competition = "Spring Festival"
        club = "Simply Lift"
        url = '/book/{}/{}'.format(competition,club)
        self.client.get(url)

    @task
    def purchasePlaces(self):
        placesRequired = 9
        competition = "Spring Festival"
        club = "Simply Lift"
        self.client.post('/purchasePlaces', data={"competition":competition,"club":club,"places":placesRequired})
