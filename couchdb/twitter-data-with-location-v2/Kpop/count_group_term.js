function(doc) {
    boys=['BTS','#BTS','NCT','#NCT','EXO','#EXO','#SEVENTEEN','GOT7','#GOT7','#StrayKids','Stray Kids','StrayKids','ATEEZ','#ATEEZ',
    '#TXT','Super Junior','#SuperJunior','SuperJunior','#ENHYPEN','ENHYPEN',
    '#WINNER','#ikon','ikon','astro','#astro']
    girls=['#blackpink','blackpink',
    '#TWICE','Red Velvet','RedVelvet','#RedVelvet','#ITZY','ITZY','#MAMAMOO','MAMAMOO','kepler','#kepler',
    'gidle','#gidle','GFRIEND','#GFRIEND','#IZONE','IZONE','aespa','#aespa','NMIXX','#NMIXX','ive','#ive','le sserafim','#newjeans','new jeans',
    'lesserafim','#lesserafim']
    var boys_pattern = RegExp("\\b(" + boys.join("|") + ")\\b", "gi");
    var girls_pattern = RegExp("\\b(" + girls.join("|") + ")\\b", "gi");
    var boys_matches = (doc.text || "").match(boys_pattern) || [];
    var girls_matches = (doc.text || "").match(girls_pattern) || [];
    if (boys_matches.length > 0 && girls_matches.length>0) {
        emit(doc.state_code, {'boys': 1 ,'girls': 1, 'total': 2});
      }
    else if(boys_matches.length > 0 ){
      emit(doc.state_code, {'boys': 1 ,'girls': 0, 'total': 1});
    }
    else if(girls_matches.length > 0 ){
      emit(doc.state_code, {'boys': 0 ,'girls': 1, 'total': 1});
    }
}

_sum