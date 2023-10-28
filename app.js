const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

app.use(bodyParser.json());

const decisionTree = require('./decisionTree.json');

app.post('/traverse', (req, res) => {
  const answers = req.body.answers || [];
  let currentTree = decisionTree;

  for (let answer of answers) {
    const index = currentTree.options.indexOf(answer);
    if (index === -1 || !currentTree.next) {
      return res.status(400).json({ error: 'Invalid answers provided.' });
    }
    currentTree = currentTree.next[index];
  }

  if (typeof currentTree === 'string') {
    return res.json({ message: currentTree });
  } else {
    return res.json(currentTree);
  }
});

app.listen(PORT, () => {
  console.log(`Server started on http://localhost:${PORT}`);
});
