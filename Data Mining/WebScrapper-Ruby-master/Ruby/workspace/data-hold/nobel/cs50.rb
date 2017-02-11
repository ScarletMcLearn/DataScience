require 'nokogiri'
require 'open-uri'
require 'csv'

doc = Nokogiri::HTML(open("https://boston.craigslist.org/search/bik"))

path = doc.css("span.txt a")[0]['href']
# puts path


item = Nokogiri::HTML(open("https://boston.craigslist.org#{path}"))
description = item.at_css("section#postingbody").text


# fname = "description.txt"
# file = File.open(fname, "w")
# file.puts description
# file.close



title = []
price = []
description = []
paths = []
url = []


doc.css("span.txt").each do |link|
    paths << link.css("a.hdrlnk")[0]['href']
    # puts link.css("span.price").text
end


puts "accessing links"



# paths.each_with_index do |path, index|
#     item_page = Nokogiri::HTML(open("https://boston.craigslist.org#{path}"))
#     puts "Accessing page #{index}"
#     title << item_page.css("span.postingtitletext").text
#     price << item_page.css("span.price").text
#     description << item_page.css("section#postingbody").text
#     url << "https://boston.craigslist.org#{path}"
# end



for index in 0..3 do
    item_page = Nokogiri::HTML(open("https://boston.craigslist.org#{path}"))
    puts "Accessing page #{index}"
    title << item_page.css("span.postingtitletext").text
    price << item_page.css("span.price").text
    description << item_page.css("section#postingbody").text
    url << "https://boston.craigslist.org#{path}"
end


puts title
puts price
puts description
puts url


CSV.open("craigslistbikes.csv", "w") do |csv|
    puts "Writing to CSV..."
    csv << title
    csv << price
    csv << url
    csv << description
    puts "Success"
end