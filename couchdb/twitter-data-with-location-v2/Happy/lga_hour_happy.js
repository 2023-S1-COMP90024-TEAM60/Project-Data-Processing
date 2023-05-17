function(doc) {
    if (doc.sentiment && doc.lga_code!='0'&& doc.created_at) {
      var date = new Date(doc.created_at);
      emit([doc.lga_code, date.getUTCHours()], { sentiment: doc.sentiment, num: 1 });
    }
  }

function(keys, values, rereduce) {
    var result = { num: 0, sentiment: 0 };
    for (var i = 0; i < values.length; i++) {
      result.sentiment += values[i].sentiment;
      result.num += values[i].num;
    }
    result.sentiment = result.sentiment / result.num;
    return result;
}