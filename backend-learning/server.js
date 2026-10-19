require("dotenv").config();

const express = require("express");
const app = express();

const PORT = process.env.PORT


app.listen(PORT, () => {
    console.log(`${process.env.APP_NAME} runnimg on port ${PORT}`);
});

app.get("/", (req, res) => {
    res.send("from backent");
});

app.listen(3000, () => {
    console.log("server running")
})

