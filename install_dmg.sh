MOUNTDIR=$(echo `hdiutil mount "$1" | tail -1 | awk '{$1=$2=""; print $0}'` | xargs -0 echo)

echo "### CHECKING .mpkg FILES ###"
sudo installer -verbose -pkg "${MOUNTDIR}/"*.mpkg -target /
echo "### CHECKING .pkg FILES ###"
sudo installer -verbose -pkg "${MOUNTDIR}/"*.pkg -target /
sudo hdiutil unmount "${MOUNTDIR}"
