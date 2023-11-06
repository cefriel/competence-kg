URL="https://knowledge.c-innovationhub.com/competence-kg/schema"

# Base IRI
echo "▶️ $URL"
echo "Accept: */* [Expected: rdf/xml]"
curl -s -I -L $URL | grep 'Content-Type:' | awk {'print $2'}
echo "-------------"
echo "Result"
curl -L $URL
echo "-------------"
echo "Accept: text/html [Expected: html]"
curl -s -I -L -H "Accept: text/html" $URL | grep 'Content-Type:' | awk {'print $2'}
echo "-------------"
echo "Accept: text/turtle [Expected: turtle]"
curl -s -I -L -H "Accept: text/turtle" $URL | grep 'Content-Type:' | awk {'print $2'}
echo "-------------"
echo "Accept: application/rdf+xml [Expected: rdf+xml]"
curl -s -I -L -H "Accept: application/rdf+xml" $URL | grep 'Content-Type:' | awk {'print $2'}
echo "-------------"
echo "Resource not available [Expected: 406]"
curl -s -I -L -H "Accept: application/foo" $URL | grep 'Content-Type:' | awk {'print $2'}
echo "-------------"
echo "Empty accept [Expected: 406]"
curl -s -I -L -H "Accept: " $URL | grep 'Content-Type::' | awk {'print $2'}
echo "-------------"