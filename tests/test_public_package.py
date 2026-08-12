import json,pathlib,subprocess,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
@unittest.skipUnless((ROOT/"public-content-manifest.json").is_file(),"projected public tree only")
class PublicPackageTests(unittest.TestCase):
 def test_manifest_and_public_links(self):
  manifest=json.loads((ROOT/"public-content-manifest.json").read_text()); self.assertNotIn("source_sha",manifest)
  for item in manifest["files"]: self.assertTrue((ROOT/item["path"]).is_file())
  for path in [ROOT/"README.md",ROOT/"SECURITY.md",*ROOT.glob("plugins/intent-to-release/**/*.md")]: self.assertNotIn("/Users/",path.read_text(errors="replace"))
if __name__=="__main__": unittest.main()
