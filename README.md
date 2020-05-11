# DVD-RENAMER

Scan a directory for mkv files search the name against IMDB and take results and rename file to a friendlier format for Plex with a format of `./Title (Year)/Title (Year).mkv`

There are 3 volumes that need to created:
* `/source`: this is the folder that will be watched for files to be dumped into
* `/destination`: this is the folder where the videos will be placed into
* `/trash`: If something goes wrong or the name is a duplicate of an existing directory the files will be placed here with correct naming, and you can deal with the file as you please


You will also need to create a API key at for this at http://www.omdbapi.com/apikey.aspx and set it to enviorment variable `APIKEY`

Docker Example
'''docker -d run -v "./rip:/source" -v "./plex/video:/destination" -v "./riptrash:/trash" -e "APIKEY=3af99f68" --name dvd-renamer malmon/dvd-renamer:latest'''