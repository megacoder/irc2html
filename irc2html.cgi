<HTML>
 <HEAD>
  <TITLE>irc2html.cgi</TITLE>
 </HEAD>
 <BODY>
  <FORM METHOD=POST>
   <TABLE>
    <TR>
     <TD COLSPAN=2 VALIGN=TOP ALIGN=CENTER>
      <DIV ALIGN=CENTER>
       <B><SPAN STYLE='font-size:larger'>Chat log to HTML Converter<BR></SPAN>
        by <A HREF="http://www.jwz.org/">Jamie Zawinski</A><BR>
        Version <A HREF="http://www.jwz.org/hacks/irc2html.pl">1.23</A>
      </SPAN>
      Paste your IRC/AIM log here:</B><BR>
      <TEXTAREA NAME="body" ROWS=10 COLS=60 WRAP=OFF></TEXTAREA>
     </TD>
    </TR>
    <TR>
     <TD VALIGN=TOP ALIGN=LEFT NOWRAP>
      <INPUT NAME="strip_status" TYPE=CHECKBOX> Strip Status Lines<BR>
      <INPUT NAME="strip_timestamps" TYPE=CHECKBOX> Strip Timestamps<BR>
      <INPUT NAME="colorize" TYPE=CHECKBOX CHECKED> Colorize
     </TD>
     <TD VALIGN=MIDDLE ALIGN=RIGHT NOWRAP>
      <INPUT TYPE=SUBMIT VALUE="Generate HTML">
      &nbsp; &nbsp; &nbsp; 
      <INPUT TYPE=RESET VALUE="Clear">
     </TD>
    </TR>
   </TABLE>
  </FORM>
 </BODY>
</HTML>
