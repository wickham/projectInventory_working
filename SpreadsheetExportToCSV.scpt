FasdUAS 1.101.10   ��   ��    k             l     ��  ��     ! /usr/bin/osascript     � 	 	 ( !   / u s r / b i n / o s a s c r i p t   
  
 l     ��������  ��  ��        l      ��  ��   60
---------------------------------------------------------------------------------
 
 Script: SpreadsheetExportToCSV
 
 Command-line tool to convert a spreadsheet document to CSV
 This AppleScript is tested with and compatible with Apple iWork Numbers 3.6,
 current as at October 23, 2015.
 
 Parameters:
 1. Full Path to the input file, including file extension
 2. Full Path to the output file, including file extension
 
 Example command-line invocation:
 
    osascript SpreadsheetExportToCSV.scpt "/Users/me/Documents/MySpreadsheet.xlsx" "/Users/me/Documents/Converted/OutputFile.csv"
 
 The spreadsheet to use as an input file can be an Excel file or a Numbers file.
 
 Original Author:
 Sohail Ahmed
 Blog: http://sohail.io
 

---------------------------------------------------------------------------------
     �  ` 
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
   
   S c r i p t :   S p r e a d s h e e t E x p o r t T o C S V 
   
   C o m m a n d - l i n e   t o o l   t o   c o n v e r t   a   s p r e a d s h e e t   d o c u m e n t   t o   C S V 
   T h i s   A p p l e S c r i p t   i s   t e s t e d   w i t h   a n d   c o m p a t i b l e   w i t h   A p p l e   i W o r k   N u m b e r s   3 . 6 , 
   c u r r e n t   a s   a t   O c t o b e r   2 3 ,   2 0 1 5 . 
   
   P a r a m e t e r s : 
   1 .   F u l l   P a t h   t o   t h e   i n p u t   f i l e ,   i n c l u d i n g   f i l e   e x t e n s i o n 
   2 .   F u l l   P a t h   t o   t h e   o u t p u t   f i l e ,   i n c l u d i n g   f i l e   e x t e n s i o n 
   
   E x a m p l e   c o m m a n d - l i n e   i n v o c a t i o n : 
   
         o s a s c r i p t   S p r e a d s h e e t E x p o r t T o C S V . s c p t   " / U s e r s / m e / D o c u m e n t s / M y S p r e a d s h e e t . x l s x "   " / U s e r s / m e / D o c u m e n t s / C o n v e r t e d / O u t p u t F i l e . c s v " 
   
   T h e   s p r e a d s h e e t   t o   u s e   a s   a n   i n p u t   f i l e   c a n   b e   a n   E x c e l   f i l e   o r   a   N u m b e r s   f i l e . 
   
   O r i g i n a l   A u t h o r : 
   S o h a i l   A h m e d 
   B l o g :   h t t p : / / s o h a i l . i o 
   
 
 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
      l     ��������  ��  ��        p         ������ *0 _inputfilepathalias _inputFilePathAlias��        p         ������ "0 _outputfilepath _outputFilePath��        p         ������ &0 _requestedoptions _requestedOptions��        l     ��������  ��  ��        l     ��������  ��  ��       !   l      �� " #��   " � �
 run
 
 This is our entry point, our main function, where this script 
 begins execution. We call out to helper functions, to modularize
 the design.
    # � $ $. 
   r u n 
   
   T h i s   i s   o u r   e n t r y   p o i n t ,   o u r   m a i n   f u n c t i o n ,   w h e r e   t h i s   s c r i p t   
   b e g i n s   e x e c u t i o n .   W e   c a l l   o u t   t o   h e l p e r   f u n c t i o n s ,   t o   m o d u l a r i z e 
   t h e   d e s i g n . 
 !  % & % i      ' ( ' I     �� )��
�� .aevtoappnull  �   � **** ) o      ���� 0 argv  ��   ( k      * *  + , + l     �� - .��   - 3 - Ensure our CSV files are encoding with UTF8:    . � / / Z   E n s u r e   o u r   C S V   f i l e s   a r e   e n c o d i n g   w i t h   U T F 8 : ,  0 1 0 I     �������� (0 ensureutf8encoding ensureUTF8Encoding��  ��   1  2 3 2 l   ��������  ��  ��   3  4 5 4 l   �� 6 7��   6 . ( Parse and determine input/output paths:    7 � 8 8 P   P a r s e   a n d   d e t e r m i n e   i n p u t / o u t p u t   p a t h s : 5  9 : 9 I    �� ;���� <0 retrievecommandlinearguments retrieveCommandLineArguments ;  <�� < o    ���� 0 argv  ��  ��   :  = > = l   ��������  ��  ��   >  ? @ ? l   �� A B��   A D > Perform the actual activation, file open, export and cleanup:    B � C C |   P e r f o r m   t h e   a c t u a l   a c t i v a t i o n ,   f i l e   o p e n ,   e x p o r t   a n d   c l e a n u p : @  D E D I    �������� (0 processspreadsheet processSpreadsheet��  ��   E  F�� F l   ��������  ��  ��  ��   &  G H G l     ��������  ��  ��   H  I J I l     ��������  ��  ��   J  K L K l     ��������  ��  ��   L  M N M l     �� O P��   O J D-------------------- SUPPORTING FUNCTIONS --------------------------    P � Q Q � - - - - - - - - - - - - - - - - - - - -   S U P P O R T I N G   F U N C T I O N S   - - - - - - - - - - - - - - - - - - - - - - - - - - N  R S R l     ��������  ��  ��   S  T U T l      �� V W��   V � �
 retrieveCommandLineArguments
 
 Handles parsing the command line arguments passed to us.
 We return a list, where the first element is the input file
 path as an alias. The second element is the output path,
 as text (as it may not yet exist).
    W � X X� 
   r e t r i e v e C o m m a n d L i n e A r g u m e n t s 
   
   H a n d l e s   p a r s i n g   t h e   c o m m a n d   l i n e   a r g u m e n t s   p a s s e d   t o   u s . 
   W e   r e t u r n   a   l i s t ,   w h e r e   t h e   f i r s t   e l e m e n t   i s   t h e   i n p u t   f i l e 
   p a t h   a s   a n   a l i a s .   T h e   s e c o n d   e l e m e n t   i s   t h e   o u t p u t   p a t h , 
   a s   t e x t   ( a s   i t   m a y   n o t   y e t   e x i s t ) . 
 U  Y Z Y i     [ \ [ I      �� ]���� <0 retrievecommandlinearguments retrieveCommandLineArguments ]  ^�� ^ o      ���� 0 command_line_arguments  ��  ��   \ k     + _ _  ` a ` r      b c b c     
 d e d 4     �� f
�� 
psxf f l    g���� g n     h i h 4    �� j
�� 
cobj j m    ����  i o    ���� 0 command_line_arguments  ��  ��   e m    	��
�� 
alis c o      ���� *0 _inputfilepathalias _inputFilePathAlias a  k l k r     m n m c     o p o l    q���� q 4    �� r
�� 
psxf r l    s���� s n     t u t 4    �� v
�� 
cobj v m    ����  u o    ���� 0 command_line_arguments  ��  ��  ��  ��   p m    ��
�� 
ctxt n o      ���� "0 _outputfilepath _outputFilePath l  w x w l   ��������  ��  ��   x  y z y I   !�� {��
�� .ascrcmnt****      � **** { b     | } | m     ~ ~ �   ( i n p u t   f i l e   p a t h   i s :   } o    ���� *0 _inputfilepathalias _inputFilePathAlias��   z  � � � I  " )�� ���
�� .ascrcmnt****      � **** � b   " % � � � m   " # � � � � � * o u t p u t   f i l e   p a t h   i s :   � o   # $���� "0 _outputfilepath _outputFilePath��   �  ��� � l  * *��������  ��  ��  ��   Z  � � � l     ��������  ��  ��   �  � � � l     ��������  ��  ��   �  � � � l      �� � ���   � � �
 processSpreadsheet
 
 This function is the workhorse of this script. We open Numbers,
 have it load the source spreadsheet, and invoke the export command
 to ultimately write the output CSV to the specified path.
    � � � �� 
   p r o c e s s S p r e a d s h e e t 
   
   T h i s   f u n c t i o n   i s   t h e   w o r k h o r s e   o f   t h i s   s c r i p t .   W e   o p e n   N u m b e r s , 
   h a v e   i t   l o a d   t h e   s o u r c e   s p r e a d s h e e t ,   a n d   i n v o k e   t h e   e x p o r t   c o m m a n d 
   t o   u l t i m a t e l y   w r i t e   t h e   o u t p u t   C S V   t o   t h e   s p e c i f i e d   p a t h . 
 �  � � � i     � � � I      �������� (0 processspreadsheet processSpreadsheet��  ��   � O     { � � � k    z � �  � � � I   	������
�� .miscactvnull��� ��� null��  ��   �  � � � l  
 
��������  ��  ��   �  � � � l  
 
�� � ���   � E ? Before we open the file asked of us, close out every document     � � � � ~   B e f o r e   w e   o p e n   t h e   f i l e   a s k e d   o f   u s ,   c l o s e   o u t   e v e r y   d o c u m e n t   �  � � � l  
 
�� � ���   � J D that might have opened along with the application having activated:    � � � � �   t h a t   m i g h t   h a v e   o p e n e d   a l o n g   w i t h   t h e   a p p l i c a t i o n   h a v i n g   a c t i v a t e d : �  � � � I  
 �� � �
�� .coreclosnull���     obj  � 2   
 ��
�� 
cwin � �� ���
�� 
savo � m    ��
�� savono  ��   �  � � � l   ��������  ��  ��   �  � � � l   �� � ���   � 2 , Retrieve information about the source file:    � � � � X   R e t r i e v e   i n f o r m a t i o n   a b o u t   t h e   s o u r c e   f i l e : �  � � � r     � � � l    ����� � I   �� ���
�� .sysonfo4asfe        file � l    ���~ � o    �}�} *0 _inputfilepathalias _inputFilePathAlias�  �~  ��  ��  ��   � o      �|�| 0 fileinfo fileInfo �  � � � r    ! � � � n     � � � 1    �{
�{ 
pnam � l    ��z�y � o    �x�x 0 fileinfo fileInfo�z  �y   � o      �w�w 0 filename fileName �  � � � r   " ' � � � n   " % � � � 1   # %�v
�v 
nmxt � l  " # ��u�t � o   " #�s�s 0 fileinfo fileInfo�u  �t   � o      �r�r 0 fileextension fileExtension �  � � � I  ( 1�q ��p
�q .ascrcmnt****      � **** � b   ( - � � � b   ( + � � � m   ( ) � � � � � 0 O p e n i n g   s o u r c e   d o c u m e n t   � o   ) *�o�o 0 filename fileName � m   + , � � � � �  . . .�p   �  � � � l  2 2�n�m�l�n  �m  �l   �  � � � O   2 r � � � k   : q � �  � � � l  : :�k � ��k   � Q K In this scope, we are now implicitly dealing with the document just opened    � � � � �   I n   t h i s   s c o p e ,   w e   a r e   n o w   i m p l i c i t l y   d e a l i n g   w i t h   t h e   d o c u m e n t   j u s t   o p e n e d �  � � � l  : :�j � ��j   � P J as the current target, which means we access it through the "it" keyword,    � � � � �   a s   t h e   c u r r e n t   t a r g e t ,   w h i c h   m e a n s   w e   a c c e s s   i t   t h r o u g h   t h e   " i t "   k e y w o r d , �  � � � l  : :�i � ��i   � � � as per: https://developer.apple.com/library/mac/documentation/AppleScript/Conceptual/AppleScriptLangGuide/conceptual/ASLR_fundamentals.html#//apple_ref/doc/uid/TP40000983-CH218-SW4    � � � �j   a s   p e r :   h t t p s : / / d e v e l o p e r . a p p l e . c o m / l i b r a r y / m a c / d o c u m e n t a t i o n / A p p l e S c r i p t / C o n c e p t u a l / A p p l e S c r i p t L a n g G u i d e / c o n c e p t u a l / A S L R _ f u n d a m e n t a l s . h t m l # / / a p p l e _ r e f / d o c / u i d / T P 4 0 0 0 0 9 8 3 - C H 2 1 8 - S W 4 �  � � � l  : :�h�g�f�h  �g  �f   �  � � � r   : = � � �  g   : ; � o      �e�e  0 activedocument activeDocument �  � � � l  > >�d�c�b�d  �c  �b   �  � � � l  > >�a � ��a   � ` Z Note: We could have also gotten to the active document by walking the chain from the top,    � � � � �   N o t e :   W e   c o u l d   h a v e   a l s o   g o t t e n   t o   t h e   a c t i v e   d o c u m e n t   b y   w a l k i n g   t h e   c h a i n   f r o m   t h e   t o p , �  � � � l  > >�` � ��`   � . ( i.e. right from the Application object:    � � � � P   i . e .   r i g h t   f r o m   t h e   A p p l i c a t i o n   o b j e c t : �  � � � l  > >�_ � ��_   � @ :set activeDocument to document 1 of application "Numbers"     � � � � t s e t   a c t i v e D o c u m e n t   t o   d o c u m e n t   1   o f   a p p l i c a t i o n   " N u m b e r s "   �  �  � l  > >�^�]�\�^  �]  �\     I  > C�[�Z
�[ .sysottosnull���     TEXT m   > ? �  S t a r t i n g   E x p o r t�Z    t   D c	 k   H b

  I  H `�Y
�Y .Nmstexponull���     docu o   H I�X�X  0 activedocument activeDocument �W
�W 
exft m   L O�V
�V NmefNcsv �U�T
�U 
pfil 4   R Z�S
�S 
file o   V Y�R�R "0 _outputfilepath _outputFilePath�T    l  a a�Q�Q   7 1 Use this instead if you want to export to Excel:    � b   U s e   t h i s   i n s t e a d   i f   y o u   w a n t   t o   e x p o r t   t o   E x c e l : �P l  a a�O�O   H B export activeDocument as Microsoft Excel to file _outputFilePath     � �   e x p o r t   a c t i v e D o c u m e n t   a s   M i c r o s o f t   E x c e l   t o   f i l e   _ o u t p u t F i l e P a t h  �P  	 m   D G�N�NX  I  d k�M�L
�M .sysottosnull���     TEXT m   d g �   " C o m p l e t e d   E x p o r t .�L   !"! l  l l�K�J�I�K  �J  �I  " #$# l  l l�H%&�H  % I C Since we closed out other windows that might have been open before   & �'' �   S i n c e   w e   c l o s e d   o u t   o t h e r   w i n d o w s   t h a t   m i g h t   h a v e   b e e n   o p e n   b e f o r e$ ()( l  l l�G*+�G  * J D opening the file we sought, we really should only have one document   + �,, �   o p e n i n g   t h e   f i l e   w e   s o u g h t ,   w e   r e a l l y   s h o u l d   o n l y   h a v e   o n e   d o c u m e n t) -.- l  l l�F/0�F  /   window open.   0 �11    w i n d o w   o p e n .. 2�E2 I  l q�D3�C
�D .coreclosnull���     obj 3 o   l m�B�B  0 activedocument activeDocument�C  �E   � l  2 74�A�@4 I  2 7�?5�>
�? .aevtodocnull  �    alis5 o   2 3�=�= *0 _inputfilepathalias _inputFilePathAlias�>  �A  �@   � 676 l  s s�<�;�:�<  �;  �:  7 898 l  s s�9�8�7�9  �8  �7  9 :;: I  s x�6�5�4
�6 .aevtquitnull��� ��� null�5  �4  ; <=< l  y y�3�2�1�3  �2  �1  = >�0> l  y y�/�.�-�/  �.  �-  �0   � m     ??�                                                                                  NMBR  alis    6  Mac                        ���H+   uNumbers.app                                                     /�m�;J�        ����  	                Applications    �+      �;�     u  Mac:Applications: Numbers.app     N u m b e r s . a p p    M a c  Applications/Numbers.app  / ��   � @A@ l     �,�+�*�,  �+  �*  A BCB l     �)�(�'�)  �(  �'  C DED l      �&FG�&  F��
 ensureUTF8Encoding
 
 Microsoft Excel on the Mac is not good with exporting special
 characters as is Apple Numbers. Part of this is in the ability for
 Numbers to correctly process UTF8 formatting when exporting.
 
 Setup default export encoding for CSV files to UTF8, so without 
 specifying anything further for AppleScript, the right format will 
 be applied automatically. Since we cannot specify the CSV export
 encoding via AppleScript, we will set it via the Defaults Database
 with a shell command.
 
 Here are the codes that apply: 4=UTF8, 12=windows latin, 30=MacRoman
 As such, we'll specify 4 for UTF8.
 
 This technique courtesy of: https://discussions.apple.com/thread/4018778?tstart=0 
   G �HH� 
   e n s u r e U T F 8 E n c o d i n g 
   
   M i c r o s o f t   E x c e l   o n   t h e   M a c   i s   n o t   g o o d   w i t h   e x p o r t i n g   s p e c i a l 
   c h a r a c t e r s   a s   i s   A p p l e   N u m b e r s .   P a r t   o f   t h i s   i s   i n   t h e   a b i l i t y   f o r 
   N u m b e r s   t o   c o r r e c t l y   p r o c e s s   U T F 8   f o r m a t t i n g   w h e n   e x p o r t i n g . 
   
   S e t u p   d e f a u l t   e x p o r t   e n c o d i n g   f o r   C S V   f i l e s   t o   U T F 8 ,   s o   w i t h o u t   
   s p e c i f y i n g   a n y t h i n g   f u r t h e r   f o r   A p p l e S c r i p t ,   t h e   r i g h t   f o r m a t   w i l l   
   b e   a p p l i e d   a u t o m a t i c a l l y .   S i n c e   w e   c a n n o t   s p e c i f y   t h e   C S V   e x p o r t 
   e n c o d i n g   v i a   A p p l e S c r i p t ,   w e   w i l l   s e t   i t   v i a   t h e   D e f a u l t s   D a t a b a s e 
   w i t h   a   s h e l l   c o m m a n d . 
   
   H e r e   a r e   t h e   c o d e s   t h a t   a p p l y :   4 = U T F 8 ,   1 2 = w i n d o w s   l a t i n ,   3 0 = M a c R o m a n 
   A s   s u c h ,   w e ' l l   s p e c i f y   4   f o r   U T F 8 . 
   
   T h i s   t e c h n i q u e   c o u r t e s y   o f :   h t t p s : / / d i s c u s s i o n s . a p p l e . c o m / t h r e a d / 4 0 1 8 7 7 8 ? t s t a r t = 0   
E I�%I i    JKJ I      �$�#�"�$ (0 ensureutf8encoding ensureUTF8Encoding�#  �"  K I    �!L� 
�! .sysoexecTEXT���     TEXTL m     MM �NN � / u s r / b i n / d e f a u l t s   w r i t e   c o m . a p p l e . i W o r k . N u m b e r s   C S V E x p o r t E n c o d i n g   - i n t   4�   �%       
�OPQRSTU���  O ��������
� .aevtoappnull  �   � ****� <0 retrievecommandlinearguments retrieveCommandLineArguments� (0 processspreadsheet processSpreadsheet� (0 ensureutf8encoding ensureUTF8Encoding� *0 _inputfilepathalias _inputFilePathAlias� "0 _outputfilepath _outputFilePath�  �  P � (��VW�
� .aevtoappnull  �   � ****� 0 argv  �  V �� 0 argv  W ���� (0 ensureutf8encoding ensureUTF8Encoding� <0 retrievecommandlinearguments retrieveCommandLineArguments� (0 processspreadsheet processSpreadsheet� *j+  O*�k+ O*j+ OPQ � \��
XY�	� <0 retrievecommandlinearguments retrieveCommandLineArguments� �Z� Z  �� 0 command_line_arguments  �
  X �� 0 command_line_arguments  Y 	������  ~�� �
� 
psxf
� 
cobj
� 
alis� *0 _inputfilepathalias _inputFilePathAlias
� 
ctxt�  "0 _outputfilepath _outputFilePath
�� .ascrcmnt****      � ****�	 ,*��k/E/�&E�O*��l/E/�&E�O��%j O��%j OPR �� �����[\���� (0 processspreadsheet processSpreadsheet��  ��  [ ���������� 0 fileinfo fileInfo�� 0 filename fileName�� 0 fileextension fileExtension��  0 activedocument activeDocument\ ?������������������ � �������������������������
�� .miscactvnull��� ��� null
�� 
cwin
�� 
savo
�� savono  
�� .coreclosnull���     obj �� *0 _inputfilepathalias _inputFilePathAlias
�� .sysonfo4asfe        file
�� 
pnam
�� 
nmxt
�� .ascrcmnt****      � ****
�� .aevtodocnull  �    alis
�� .sysottosnull���     TEXT��X
�� 
exft
�� NmefNcsv
�� 
pfil
�� 
file�� "0 _outputfilepath _outputFilePath�� 
�� .Nmstexponull���     docu
�� .aevtquitnull��� ��� null�� |� x*j O*�-��l O�j E�O��,E�O��,E�O�%�%j O�j  9*E�O�j Oa n�a a a *a _ /a  OPoOa j O�j UO*j OPUS ��K����]^���� (0 ensureutf8encoding ensureUTF8Encoding��  ��  ]  ^ M��
�� .sysoexecTEXT���     TEXT�� �j TDalis    @   Mac                        ���H+   ���parts.numbers                                                   �)��9�        ����  I                 �+      ��
      p a r t s . n u m b e r s    M a c  NUsers/Allen/Current Work/CODE/projectInventory_working/Templates/parts.numbers  /    ��      U �__ � M a c : U s e r s : A l l e n : C u r r e n t   W o r k : C O D E : p r o j e c t I n v e n t o r y _ w o r k i n g : r e s u l t s�  �   ascr  ��ޭ