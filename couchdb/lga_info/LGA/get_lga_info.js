function (doc) {
  emit(doc.lga_code,[doc.lga_name,doc.ste_code,doc.ste_name]);
}