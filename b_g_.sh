#! bin/bash

echo ""
setterm -foreground green
echo "╭───────────╮"
echo "┃_____● ══__⊙°°"
echo "┃███████████┃"
echo "┃███████████┃"
echo "┃███████████┃"
echo "┃███████████┃"
echo "┃█  Android ████┃"
echo "┃███████████┃"
echo "┃███████████┃"
echo "┃███████████┃"
echo "┃███████████┃"
echo "┃███████████┃"
echo "┃            🔘"
echo "╰────────--──╯"
echo ""
while :
do
echo -e "\e[1;32m[1]-[ GENERAR BIN CON FECHA ]\e[0m"
echo -e "\e[1;32m[2]-[ GENERAR BIN RANDOM ]\e[0m"
echo ""
echo -e -n "\e[1;31m》》》\e[0m "
read opcion
case $opcion in
1)
#! bin/bash
echo ""
python bfc.py
exit
;;
2)
#/ bin/bash
echo ""
python bnd.py
exit
;;
esac
done

