function (doc) {
    emit([doc.state_code,doc.lga_code], {'population':doc.population,'area(km2)':doc.area});
  }

_sum
