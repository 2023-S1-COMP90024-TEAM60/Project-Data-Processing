function(doc) {
    targets=['covid-19', 'covid', 'pandemic', 'coronavirus', 'sars-cov-2', 'pfizer', 'moderna','quarantine','social distancing','pcr test','Vaccination','pcrtest', 'rat test', 'rattest']
    var pattern = RegExp("\\b(" + targets.join("|") + ")\\b", "gi");
    var matches = (doc.content || "").match(pattern) || [];
    if (matches.length > 0) {
        emit(matches[0].replace(/^#\s*/, '').toLowerCase(), 1);
      }
  }


_sum