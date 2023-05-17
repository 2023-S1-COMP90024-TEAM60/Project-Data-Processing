function(doc) {
    if (doc.sentiment && doc.created_at) {
      var date = new Date(doc.created_at);
      var hour=date.getUTCHours();
      dict={}
      for (var i = 0; i < 24; i++) {
        dict[i] = {sentiment: 0};
      }
      dict[hour]=doc.sentiment
      emit(doc.state_code, dict);
    }
}
function(keys, values, rereduce) {
    var output = {};
    for (var i = 0; i < 24; i++) {
      var total = 0;
      var count = 0;
      for (var j = 0; j < values.length; j++) {
        if (values[j][i] !== undefined) {
          total += values[j][i];
          count++;
        }
      }
      output[i] = count > 0 ? total / count : 0;
    }
    return output;
}