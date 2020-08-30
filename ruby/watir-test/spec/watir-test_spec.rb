require "watir"
require "webdrivers"


RSpec.describe Tutorial do
   it "should logon to linkedin" do
      browser = Watir::Browser.new
      browser.goto 'https://linkedin.com/login'

      # check that the login fields exist      
      expect(browser.text_field(id: "username").exists?).to equal(true)
      expect(browser.text_field(id: "password").exists?).to equal(true)
      
 
      #expect(browser.checkbox(id: "rememberMeOptIn-checkbox").exists?).to equal(false)

      # set the login fields
      browser.text_field(id: "username").set "<insert username to test>"
      browser.text_field(id: "password").set "<insert password to test>"

     
      # set the remember me checkbox
      #browser.checkbox(id: "rememberMeOptIn-checkbox").set 

      browser.button(type: "submit").click
      
   end
      
end
