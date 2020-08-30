# -*- encoding: utf-8 -*-
# stub: watir 4.0.2 ruby lib

Gem::Specification.new do |s|
  s.name = "watir".freeze
  s.version = "4.0.2"

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Bret Pettichord".freeze]
  s.date = "2012-10-31"
  s.description = "Automated testing tool for web applications. By Testers. For Testers.".freeze
  s.email = ["bret@pettichord.com".freeze]
  s.homepage = "http://github.com/watir/watir".freeze
  s.rubygems_version = "3.0.3".freeze
  s.summary = "Watir".freeze

  s.installed_by_version = "3.0.3" if s.respond_to? :installed_by_version

  if s.respond_to? :specification_version then
    s.specification_version = 3

    if Gem::Version.new(Gem::VERSION) >= Gem::Version.new('1.2.0') then
      s.add_runtime_dependency(%q<commonwatir>.freeze, ["~> 4"])
      s.add_runtime_dependency(%q<watir-webdriver>.freeze, [">= 0"])
    else
      s.add_dependency(%q<commonwatir>.freeze, ["~> 4"])
      s.add_dependency(%q<watir-webdriver>.freeze, [">= 0"])
    end
  else
    s.add_dependency(%q<commonwatir>.freeze, ["~> 4"])
    s.add_dependency(%q<watir-webdriver>.freeze, [">= 0"])
  end
end
