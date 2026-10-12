import assert from "node:assert/strict"
import test from "node:test"
import { registryGreeting } from "./index.js"

test("returns a stable greeting", () => {
  assert.equal(registryGreeting("CI"), "Hello, CI, from a private Ravenstash package.")
})
