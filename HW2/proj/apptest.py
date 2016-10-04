class AppTest(unittest.TestCase):
    def setUp(self):
        # Create a WSGI application.
        app = webapp2.WSGIApplication([('/', Handler)])
        # Wrap the app with WebTest’s TestApp.
        self.testapp = webtest.TestApp(app)

    # Test the handler.
    def testHandler(self):
        homepage_response = self.testapp.get('/')
        self.assertEqual(homepage_response.status_int, 200)

        create_response = self.testapp.get('/create')
        self.assertEqual(create_response.status_int, 200)

        host_response = self.testapp.get('/host')
        self.assertEqual(host_response.status_int, 200)

        guest_response = self.testapp.get('/guest')
        self.assertEqual(guest_response.status_int, 200)

        join_response = self.testapp.get('/join')
        self.assertEqual(join_response.status_int, 200)
