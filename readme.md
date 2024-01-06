# Automation of birthday stories

The program is used in order to create the media to be used for stories for a list of birthdays (For privacy reasons, the login credentials and birthdays used by me personally are kept in the folder previous then the one pushed to Github).

The program uses a CSV file of the following format (in my case, it is called workingsheet.csv) in order to create the image for the story.

| Name  | Month | Instagram Tag |
| ----- | ----- | ------------- |
| Jake  | 3     | jake893       |
| Peter | 8     | .peter_54     |

* The *Name* Collumn is used in order to add the name to the image, and to add it the the final file name.
* The *Month* Collumn is used in order to know which birthday stories to create.
* The *Instagram Tag*  Collumn is used in order to get the image from their profile and put in the final image.

The reason that the program is executed month by month and not only once is in order to have updated profile pictures of the people. This would be useful especially if someone has their birthday on December, it wouldn't make sense to release a birthday story of such person with an almost 1 year old outdated image.

In the case that an Instagram Tag is not present for various reason, the *Instagram Tag* field could be left empty, as follows.

| Name   | Month | Instagram Tag |
| ------ | ----- | ------------- |
| Edward | 11    |               |

If this is done, the program would output in the terminal that the story must be done manually.
