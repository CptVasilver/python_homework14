from selene import browser, have, command


class Profile:

    def open(self):
        browser.open('/')
        browser.all('.link-underlined').element_by(have.text('Reject all')).click()

    def scroll(self, tag):
        browser.element(f'.{tag}').perform(command.js.scroll_into_view)

    def choose_page(self, value):
        browser.element('.search-dropdown').click()
        browser.element(f'[data-option="{value}"]').click()

    def assert_pint(self):
        browser.element('[data-test-id="profile-name"]').should(have.text('awwwards.'))
        browser.element('[data-test-id="main-user-description-text"]').should(have.text('The awards for design, '
                                                                                        'creativity and innovation on'
                                                                                        ' the Internet, '
                                                                                        'which recognize and promote '
                                                                                        'the best web designers in '
                                                                                        'the world'))

    def assert_courses(self):
        browser.all('.filter-box__list').all('span').should(
            have.texts('Illustration', 'Marketing & Business', 'Photography & video', 'Design', '3d & Animation',
                       'Web & App Design', 'Calligraphy & Typography'))

    def login(self):
        browser.element('[data-action= "click->login#open"]').click()
        browser.element('[placeholder="Email or Username"]').type('Tester_Agent')
        browser.element('[placeholder="Password"]').type('x&Lp6zt%59z@b_7')
        browser.element('[data-controller="button-loader"]').click()

    def check_pinterest(self):
        self.scroll('footer__nav')
        browser.element('[href="https://www.pinterest.es/awwwards/"]').click()
        self.assert_pint()

    def check_coursers(self):
        self.choose_page('course')
        self.scroll('filter-box__list')
        self.assert_courses()
