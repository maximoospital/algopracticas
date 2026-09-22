import MultiplosDeN
import Test.HUnit


-- Las pruebas unitarias
testSuiteMultiplosDeN = test [
  "lista vacia" ~: (multiplosDeN 4 []) ~?= [],
  "valor 0, mult 0" ~: (multiplosDeN 0 [1,3]) ~?= [],
  "valor 0, mult 1" ~: (multiplosDeN 0 [-1,0,9]) ~?= [0],
  "valor < 0, mult 0" ~: (multiplosDeN (-3) [20,13,-4]) ~?= [],
  "valor < 0, mult 1" ~: (multiplosDeN (-8) [9,-16,7]) ~?= [-16],
  "valor < 0, mult > 1" ~: (multiplosDeN (-7) [0,-14,15]) ~?= [0,-14],
  "valor > 0, mult 0" ~: (multiplosDeN 5 [4,-7,9]) ~?= [],
  "valor > 0, mult 1" ~: (multiplosDeN 7 [7,8,-9]) ~?= [7],
  "valor > 0, mult > 1" ~: (multiplosDeN 11 [-22,10,33]) ~?= [-22,33] 
  ]

-- Correr todas las pruebas
correrTests = runTestTT testSuiteMultiplosDeN