FasdUAS 1.101.10   ��   ��    k             j     �� �� 0 appname AppName  m         OmniGraffle      	 
 	 l     ������  ��   
     l     ��  r         b         b         b         b         b     	    b         m        0 *This menu contains AppleScripts to extend      o    ���� 0 appname AppName  m       � �'s functionality; to run a script, select it in the menu. To add scripts to the menu, save them in your Library/Application Support/     o   	 ���� 0 appname AppName  m        /Scripts folder. See      o    ���� 0 appname AppName  m         Help for more info.     o      ���� 0 
dialogtext 
dialogText��       !   l     ������  ��   !  " # " l   ( $�� $ I   (�� % &
�� .sysodlogaskr        TEXT % o    ���� 0 
dialogtext 
dialogText & �� ' (
�� 
btns ' J    " ) )  * + * m     , ,  Open Scripts Folder    +  -�� - m      . .  OK   ��   ( �� /��
�� 
dflt / m   # $ 0 0  OK   ��  ��   #  1 2 1 l     ������  ��   2  3�� 3 l  )� 4�� 4 Z   )� 5 6���� 5 =  ) . 7 8 7 n   ) , 9 : 9 1   * ,��
�� 
bhit : l  ) * ;�� ; 1   ) *��
�� 
rslt��   8 m   , - < <  Open Scripts Folder    6 k   1� = =  > ? > l  1 1������  ��   ?  @ A @ l  1 @ B C B r   1 @ D E D I  1 <�� F G
�� .earsffdralis        afdr F m   1 2 H H 
 asup    G �� I��
�� 
from I m   5 8��
�� fldmfldu��   E o      ����  0 userasupfolder userAsupFolder C B < "asup" = application support folder... buggy standard osax.    A  J K J r   A R L M L I  A N�� N O
�� .earsffdralis        afdr N m   A D P P 
 asup    O �� Q��
�� 
from Q m   G J��
�� fldmfldl��   M o      ���� "0 localasupfolder localAsupFolder K  R S R Q   S v T U V T l  V g W X W r   V g Y Z Y I  V c�� [ \
�� .earsffdralis        afdr [ m   V Y ] ] 
 dlib    \ �� ^��
�� 
from ^ m   \ _��
�� fldmfldn��   Z o      ���� &0 networkdlibfolder networkDlibFolder X E ? "dlib" = library folder, since asup folder might not exist yet    U R      ������
�� .ascrerr ****      � ****��  ��   V r   o v _ ` _ m   o r a a       ` o      ���� &0 networkdlibfolder networkDlibFolder S  b c b l  w w������  ��   c  d e d Z   w � f g�� h f =  w ~ i j i o   w z���� &0 networkdlibfolder networkDlibFolder j m   z } k k       g k   � � l l  m n m I  � ��� o p
�� .sysodlogaskr        TEXT o m   � � q q � �There are two different folders you can put scripts into, depending on whether you want to keep them to yourself or share them with other people who have user accounts on this computer. Which do you want to open?    p �� r��
�� 
btns r J   � � s s  t u t m   � � v v  	My Folder    u  w�� w m   � � x x  Computer Folder   ��  ��   n  y�� y r   � � z { z n   � � | } | 1   � ���
�� 
bhit } l  � � ~�� ~ 1   � ���
�� 
rslt��   { o      ���� 0 dialogreply dialogReply��  ��   h k   � �    � � � I  � ��� � �
�� .sysodlogaskr        TEXT � m   � � � � � �There are three different folders you can put scripts into, depending on whether you want to keep them to yourself, share them with users on this computer, or share them with all users on your network. Which do you want to open?    � �� ���
�� 
btns � J   � � � �  � � � m   � � � �  	My Folder    �  � � � m   � � � �  Computer Folder    �  ��� � m   � � � �  Network Folder   ��  ��   �  ��� � r   � � � � � n   � � � � � 1   � ���
�� 
bhit � l  � � ��� � 1   � ���
�� 
rslt��   � o      ���� 0 dialogreply dialogReply��   e  � � � Z   � � � � � � � =  � � � � � o   � ����� 0 dialogreply dialogReply � m   � � � �  	My Folder    � r   � � � � � o   � �����  0 userasupfolder userAsupFolder � o      ���� 0 chosenfolder chosenFolder �  � � � =  � � � � � o   � ����� 0 dialogreply dialogReply � m   � � � �  Computer Folder    �  ��� � r   � � � � � o   � ����� "0 localasupfolder localAsupFolder � o      ���� 0 chosenfolder chosenFolder��   � r   � � � � � o   � ����� &0 networkdlibfolder networkDlibFolder � o      ���� 0 chosenfolder chosenFolder �  � � � l  � �������  ��   �  � � � l  � ��� ���   � ? 9 find out if the folder exists or if we have to create it    �  � � � r   � � � � � m   � ���
�� boovfals � o      ���� (0 shouldcreatefolder shouldCreateFolder �  � � � Z   �) � ��� � � =  � � � � � o   � ����� 0 chosenfolder chosenFolder � o   � ����� &0 networkdlibfolder networkDlibFolder � r   � � � � b   � � � � b   �	 � � � b   � � � � n   � � � � � 1   � ���
�� 
psxp � o   � ����� 0 chosenfolder chosenFolder � m   � � �  Application Support/    � o  ���� 0 appname AppName � m  	 � �  /Scripts    � o      ���� &0 scriptsfolderpath scriptsFolderPath��   � r  ) � � � b  % � � � b  ! � � � n   � � � 1  ��
�� 
psxp � o  ���� 0 chosenfolder chosenFolder � o   ���� 0 appname AppName � m  !$ � �  /Scripts    � o      ���� &0 scriptsfolderpath scriptsFolderPath �  � � � Q  *K � � � � n  -> � � � 1  9=��
�� 
asdr � l -9 ��� � I -9�� ���
�� .sysonfo4asfe       **** � 4  -5�� �
�� 
psxf � o  14���� &0 scriptsfolderpath scriptsFolderPath��  ��   � R      ������
�� .ascrerr ****      � ****��  ��   � r  FK � � � m  FG��
�� boovtrue � o      ���� (0 shouldcreatefolder shouldCreateFolder �  � � � l LL������  ��   �  � � � l LL�� ���   � n h ask if we should create the folder, and create it via the shell for quick rescursive directory creation    �  � � � Z  L� � ����� � o  LO���� (0 shouldcreatefolder shouldCreateFolder � k  R� � �  � � � I RY�� ���
�� .sysodlogaskr        TEXT � m  RU � � � |That Scripts folder doesn't exist yet. Would you like to create it now? (You may be prompted for an administrator password.)   ��   �  ��� � Q  Z� � � � � k  ]r � �  � � � I ]l�� ���
�� .sysoexecTEXT���     TEXT � b  ]h � � � b  ]d � � � m  ]` � �  
mkdir -p '    � o  `c���� &0 scriptsfolderpath scriptsFolderPath � m  dg � �  '   ��   �  ��� � r  mr � � � m  mn��
�� boovfals � o      ���� (0 shouldcreatefolder shouldCreateFolder��   � R      ������
�� .ascrerr ****      � ****��  ��   � Q  z� � � � � k  }� � �  � � � I }��� 
�� .sysoexecTEXT���     TEXT  b  }� b  }� m  }�  	mkdir -p     o  ������ &0 scriptsfolderpath scriptsFolderPath m  ��  '    ����
�� 
badm m  ���
� boovtrue��   � 	
	 r  �� m  ���~
�~ boovfals o      �}�} (0 shouldcreatefolder shouldCreateFolder
 �| l ���{�z�{  �z  �|   � R      �y�x�w
�y .ascrerr ****      � ****�x  �w   � I ���v
�v .sysodlogaskr        TEXT m  �� F @You do not have sufficent user privileges to create this folder.    �u
�u 
btns m  ��  OK    �t�s
�t 
dflt m  ��  OK   �s  ��  ��  ��   �  l ���r�q�r  �q    l ���p�p   ] W open the folder for the user using the Finder (or user's preferred Finder replacement)     Z ���o�n H  �� o  ���m�m (0 shouldcreatefolder shouldCreateFolder I ���l �k
�l .sysoexecTEXT���     TEXT  b  ��!"! b  ��#$# m  ��%%  open '   $ o  ���j�j &0 scriptsfolderpath scriptsFolderPath" m  ��&&  '   �k  �o  �n   '�i' l ���h�g�h  �g  �i  ��  ��  ��  ��       �f( )�f  ( �e�d�e 0 appname AppName
�d .aevtoappnull  �   � ****) �c*�b�a+,�`
�c .aevtoappnull  �   � ***** k    �--  ..  "//  3�_�_  �b  �a  +  , >    �^�] , .�\ 0�[�Z�Y�X < H�W�V�U�T P�S�R ]�Q�P�O�N a k q v x�M � � � � ��L ��K�J � ��I ��H�G�F � � ��E�D%&�^ 0 
dialogtext 
dialogText
�] 
btns
�\ 
dflt�[ 
�Z .sysodlogaskr        TEXT
�Y 
rslt
�X 
bhit
�W 
from
�V fldmfldu
�U .earsffdralis        afdr�T  0 userasupfolder userAsupFolder
�S fldmfldl�R "0 localasupfolder localAsupFolder
�Q fldmfldn�P &0 networkdlibfolder networkDlibFolder�O  �N  �M 0 dialogreply dialogReply�L 0 chosenfolder chosenFolder�K (0 shouldcreatefolder shouldCreateFolder
�J 
psxp�I &0 scriptsfolderpath scriptsFolderPath
�H 
psxf
�G .sysonfo4asfe       ****
�F 
asdr
�E .sysoexecTEXT���     TEXT
�D 
badm�`��b   %�%b   %�%b   %�%E�O����lv��� O��,� ��a a l E` Oa a a l E` O a a a l E` W X  a E` O_ a   a �a a  lvl O��,E` !Y a "�a #a $a %mvl O��,E` !O_ !a &  _ E` 'Y _ !a (  _ E` 'Y 	_ E` 'OfE` )O_ '_   _ 'a *,a +%b   %a ,%E` -Y _ 'a *,b   %a .%E` -O *a /_ -/j 0a 1,EW X  eE` )O_ ) ba 2j O a 3_ -%a 4%j 5OfE` )W <X    a 6_ -%a 7%a 8el 5OfE` )OPW X  a 9�a :�a ;� Y hO_ ) a <_ -%a =%j 5Y hOPY hascr  ��ޭ