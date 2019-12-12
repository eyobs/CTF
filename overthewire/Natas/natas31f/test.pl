use strict;
use warnings;
use CGI;
my $cgi= CGI->new;
if ( $cgi->upload( 'file' ) ) 
{
     my $file= $cgi->param( 'file' );
     while ( <$file> ) 
     {
         print "$_";
    }
}