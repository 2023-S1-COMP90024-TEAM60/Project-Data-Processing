function(doc) {
    if (doc.text) {
      targets=['BTS','#BTS','NCT','#NCT','EXO','#EXO','#SEVENTEEN','GOT7','#GOT7','#StrayKids','Stray Kids','StrayKids','ATEEZ','#ATEEZ',
    '#TXT','Super Junior','#SuperJunior','SuperJunior','#ENHYPEN','ENHYPEN','#WINNER','#ikon','ikon','astro','#astro','#blackpink','blackpink',
    '#TWICE','Red Velvet','RedVelvet','#RedVelvet','#ITZY','ITZY','#MAMAMOO','MAMAMOO','kepler','#kepler',
    'gidle','#gidle','GFRIEND','#GFRIEND','#IZONE','IZONE','aespa','#aespa','NMIXX','#NMIXX','ive','#ive','le sserafim','#newjeans','new jeans',
    'lesserafim','#lesserafim']
      var pattern = RegExp("\\b(" + targets.join("|") + ")\\b", "gi");
      var matches = (doc.text || "").match(pattern) || [];
      if (matches.length > 0) {
        emit(matches[0].replace(/^#\s*/, '').toLowerCase(), 1);
      }
  }
  }
_count