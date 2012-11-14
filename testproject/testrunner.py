from django.test.simple import DjangoTestSuiteRunner

class DatabaselessTestRunner(DjangoTestSuiteRunner):
    def setup_databases(self):
        pass

    def teardown_databases(self, *args):
        pass

