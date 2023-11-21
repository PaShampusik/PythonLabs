var mongoose = require("mongoose");

var Schema = mongoose.Schema;

var ProductSchema = new Schema({
    name: { type: String, required: true },
    author: { type: Schema.ObjectId, ref: "Author", required: true },
    price: { type: Number, required: true },
    description: { type: String, required: true },
    image: { type: String }
});

BookSchema.virtual("url").get(function () {
    return "/catalog/Product/" + this._id;
});

//Export model
module.exports = mongoose.model("Product", ProductSchema);