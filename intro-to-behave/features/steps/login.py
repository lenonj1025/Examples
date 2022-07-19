@given(u'that I am at the login page')
def step_impl(context):
    print("ONE")
    # INSERT Selenium WebDriver code here that will open the web browser and go to the login page


@when(u'I type a valid username for a student')
def step_impl(context):
    print("TWO")
    # Insert Selenium WebDriver code here that will type in a username into the username input box


@when(u'a valid password for the student')
def step_impl(context):
    print("THREE")
    # Insert Selenium WebDriver code here that will type in a password into the password input box


@when(u'I click login')
def step_impl(context):
    print("FOUR")
    # Insert Selenium WebDriver code that will click on the login button


@then(u'I should be redirected to the student homepage')
def step_impl(context):
    print("FIVE")
    # Insert Selenium WebDriver code that will check if we are on the student homepage

@when(u'I type in a valid username of john_doe for a student')
def step_impl(context):
    pass
    # INSERT Selenium WebDriver code that will type in john_doe in the username input


@when(u'a valid password of password12345 for the student')
def step_impl(context):
    pass
    # INSERT Selenium WebDriver code that will type in password12345 in the password input

@when(u'I type in a valid username of jane_doe for a student')
def step_impl(context):
    pass
    # INSERT Selenium WebDriver code that will type in jane_doe in the username input

@when(u'a valid password of pass123 for the student')
def step_impl(context):
    pass
    # INSERT Selenium WebDriver code that will type in pass123in the password input

@when(u'I type in a valid username of bachy21 for a student')
def step_impl(context):
    pass
    # INSERT Selenium WebDriver code that will type in bachy21 in the username input

@when(u'a valid password of password123 for the student')
def step_impl(context):
    pass
    # INSERT Selenium WebDriver code that will type in password123 in the password input

@then(u'I should be redirected to the teacher homepage')
def step_impl(context):
    pass
    # INSERT Selenium WebDriver code that will check if we are on the teacher homepage
