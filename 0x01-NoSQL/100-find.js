// 100-find.js
// This script lists all documents with names starting by "Holberton" in the "school" collection

db.school.find({ name: { $regex: /^Holberton/ } }).forEach(printjson);