function(doc) {
    if (doc.sentiment && doc.created_at) {
      var date = new Date(doc.created_at);
      var hour = date.getUTCHours();
      emit(hour, doc.sentiment);
    }
  }

_stats