const { Client } = require('pg');

const client = new Client({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false
  }
});

client.connect();

client.query('SELECT count(*) from hr;', (err, res) => {
  if (err) throw err;
  for (let row of res.rows) {
    console.log(JSON.stringify(row));
  }
  client.end();
});

// postgres://uadqvrzvvhsgvl-1:76e9e53176d897f8bb1290fec47bcdde69043710aecb602067de96961e1c7bc0@ec2-107-21-126-201.compute-1.amazonaws.com:5432/d7d2gs1qbqj579

