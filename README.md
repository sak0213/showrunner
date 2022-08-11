# showrunner

This is a project for scraping venue websites in the pgh area in order to aggregate all local events into one series of listings. And im trying to learn how to only use .py files instead of jupyter notebooks. Also, im trying out pycharm instead of vscode.
Recent Updates:
 - Scans 10 venues for new shows
   - Added a function to check if an event's unique ID is already present in DB. If true, this will instantiate the next event from a venue. False adds the event to the collection.
 - Started messing with some DB functions for selecting documents and aggregating:
{'_id': 'Brillobox', 'events': 2}
{'_id': 'Stage AE', 'events': 13}
{'_id': 'Spirit', 'events': 42}
{'_id': 'Steamworks', 'events': 68}
{'_id': 'Roxian', 'events': 24}
{'_id': 'Mr. Smalls', 'events': 53}
{'_id': 'Thunderbird', 'events': 15}
{'_id': 'Cattivo', 'events': 1}
{'_id': 'Crafthouse', 'events': 43}
{'_id': 'BlackForge', 'events': 107}
 - Next steps are to add more venues and begin building frontend


Working Event Venues:
 - Mr. Smalls - 'https://mrsmalls.com/listing/'
 - Thunderbird - 'https://thunderbirdmusichall.com/'
 - Roxian Theatre - "https://www.livenation.com/venue/KovZ917Ax13/roxian-theatre-events"
 - Cattivo - "https://cattivopgh.com/events"
 - Steamworks - "https://steamworkscreative.com/events/"
 - Brillobox - "http://www.brilloboxpgh.com/events/"
 - Spirit - "https://www.spiritpgh.com/events?view=calendar&month=06-2022"
 - Stage AE - "https://promowestlive.com/pittsburgh/stage-ae"
 - Black Forge Coffeehouse - "https://blackforgecoffee.com/pages/events"
 - Crafthouse PGH - "https://crafthousepgh.com/events-shows/"
 
Non-Working Venues:
 - "https://www.ticketweb.com/venue/club-cafe-pittsburgh-pa/23219"
   - Keep getting a 506 error

Not-Attempted:
 - https://www.livenation.com/venue/KovZpZAEk71A/the-pavilion-at-star-lake-events
 - https://www.therobotoproject.com/calendar.html
 - https://tickets-center.com/search/tickets-at-this-venue?accid=9493575329&slt=5&venueId=8437&venueName=PPG+Paints+Arena&nid=1&cid=589853664120&akwd=ppg%20paints%20arena&mt=e&network=g&dist=s&adposition=&device=c&ismobile=false&devicemodel=&placement=&target=&aceid=&random=4593690550989132516&vx=0&nid=1&accid=9493575329&campaignid=284349482&cid=589853664120&akwd=ppg%20paints%20arena&mt=e&network=g&dist=s&adposition=&device=c&ismobile=false&devicemodel=&placement=&target=&random=4593690550989132516&loc_physical_ms=9005947&loc_interest_ms=9005931&exid=17400488190&fiid=&vx=0&gclid=CjwKCAjwwo-WBhAMEiwAV4dybd5gjIJBOGDh1ysnSyYw2vb88xhD2L3tnvFLqRkEpnCZMlSdtlUdxRoCaAsQAvD_BwE
 
 
