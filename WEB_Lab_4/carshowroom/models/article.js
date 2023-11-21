var mongoose = require("mongoose");

var Schema = mongoose.Schema;

var ArticleSchema = new Schema({
    name: {
        type: String, required: true,
        max: 100, min: 3
    },
    description: {
        type: String, required: true,
        max: 3000, min: 3
    }
});

//Export model
module.exports = mongoose.model("Article", ArticleSchema);