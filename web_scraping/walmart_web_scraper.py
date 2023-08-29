import random
import requests
import json

# information on mens clothing products
url_m = "https://www.walmart.com/orchestra/snb/graphql/Browse/d01009a483e647604f8f065494542e7f315990b079a7c2405505fc52b240712b/browse?variables=%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22default%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22%22%2C%22page%22%3A2%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%225438_133197%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22%22%2C%22cat_id%22%3A%225438_133197%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22default%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22%22%2C%22page%22%3A2%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%225438_133197%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22%22%2C%22cat_id%22%3A%225438_133197%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%225438_133197%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Afalse%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchSbaTop%22%3Afalse%2C%22fetchGallery%22%3Afalse%2C%22enablePortableFacets%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFacetCount%22%3Atrue%2C%22enableFlattenedFitment%22%3Atrue%2C%22enableMultiSave%22%3Afalse%2C%22pageType%22%3A%22BrowsePage%22%7D"
headers_m = {
    'authority': 'www.walmart.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'vtc=b0aBhLSilb0AwCYpa7JkR0; TBV=7; pxcts=2b09fd5d-e3c5-11ed-9a25-4579674d6a47; _pxvid=2b09f16e-e3c5-11ed-9a25-4579674d6a47; ACID=c7b37550-19df-491c-94e5-9aa6a7b1ace0; hasACID=true; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwic3RvcmVTZWxlY3Rpb25UeXBlIjoiTFNfU0VMRUNURUQiLCJwaWNrdXAiOnsibm9kZUlkIjoiMjYyNyIsInRpbWVzdGFtcCI6MTY4MjQ2NzE0ODkwNH0sInNoaXBwaW5nQWRkcmVzcyI6eyJ0aW1lc3RhbXAiOjE2ODI0NjcxNDg5MDQsInR5cGUiOiJwYXJ0aWFsLWxvY2F0aW9uIiwiZ2lmdEFkZHJlc3MiOmZhbHNlLCJwb3N0YWxDb2RlIjoiMzM2MjAiLCJjaXR5IjoiVGFtcGEiLCJzdGF0ZSI6IkZMIiwiZGVsaXZlcnlTdG9yZUxpc3QiOlt7Im5vZGVJZCI6IjI2MjciLCJ0eXBlIjoiREVMSVZFUlkiLCJzdG9yZVNlbGVjdGlvblR5cGUiOm51bGx9XX0sInBvc3RhbENvZGUiOnsidGltZXN0YW1wIjoxNjgyNDY3MTQ4OTA0LCJiYXNlIjoiMzM2MjAifSwidmFsaWRhdGVLZXkiOiJwcm9kOnYyOmM3YjM3NTUwLTE5ZGYtNDkxYy05NGU1LTlhYTZhN2IxYWNlMCJ9; abqme=false; _pxhd=eadf3282914f024dc829e1283f6e9973e6e0bd7f2061e15e6442c57e2455c6ab:2b08d268-e3c5-11ed-ac0c-56434d66556e; _astc=6e0f72e727ebf34ef1186c75b1438fd2; mobileweb=0; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=10hNA|2s5aC|5T7w_|6mVys|7AiHj|7ZWSr|8xsUp|ACUTJ|D8jju|Hsl6B|JHHZQ|K5ar6|LHpOf|M0qc8|No0Ca|Onkhp|PuiMD|Qhov8|RKlod|ULRlt|WB4Te|X78hm|YnYws|_4HRC|_9eqK|afTN6|btMCR|bvXlL|c8tN_|ce_CN|h-QLL|hA_Hz|iiWiK|jJAPh|jzyMV|k5HHI|kHCgj|kfniS|lPtmn|pWGxn|q8ZkB|tF78O|u5Y8n|vYtA6|xMGB0|z3-UY; exp-ck=10hNA15T7w_36mVys17AiHj17ZWSr1ACUTJ2D8jju1K5ar61ULRlt2YnYws4_9eqK1afTN62ce_CN1jJAPh2jzyMV1k5HHI1lPtmn1pWGxn1q8ZkB1tF78O1u5Y8n1vYtA61z3-UY2; bstc=Xi-PkRC4Yb7dwjLx16WeTo; assortmentStoreId=2627; hasLocData=1; bm_mi=E092FD1DA4113D7B87E0027685613D28~YAAQN/vaF44zrZ6HAQAAKi8ouxPZ0xMIKVWZHUSkN05RoU96KEoZOcuHns1LNHGTT6iGiWYKQDq5MoYDl1+SklmCsxbHjL+ypx8GU1bY8rFKXvCXklp2dH188hJG7dfdmdqdJj4BLnCtv2LMfHA64lDSl4NhEv6EcwPJyKcjt29xaJ7azhEKbYWBSiPXGkT37ln96EEBVhcAa3sKrLCfhKyf3zAAYKHotRm+kZQcLs2RRkII3a/n1qe7AUbVvESLgIAE0bmXZM+mNNG9UivjGs3q61Zjsn+8a9EbzA32MrEqANyeN5CosOXYQB4/y+4hqpQO+HdmUbiQlMr6gl7VD7FjVDOcnAFfekxx~1; xptc=assortmentStoreId%2B2627; xpm=1%2B1682472186%2Bb0aBhLSilb0AwCYpa7JkR0~%2B0; bm_sv=54BF34CB2C161AB8423BBB2A0CE319C1~YAAQN/vaF+0zrZ6HAQAAozQouxNROV+mvThJ0wzNTu4l0R3mW7d3o+QbAzeSfxmQvpSy/LfvRYu7CgSOeF+YaqWxBRhDeamufy0STua6C3TkjbhyEYeLZYFPvn8pU4v31M853VJtWVC8hM2D2wrMDJuNCvsnvf/of/s2lv1XPJvZej5z+UNViMmoCvt6YS7dzMm+NtJqwchAac329aqp5MYUqvh0u6AUJIe56MKHbarezospUehQQNaAkFOqxapVsA8=~1; ak_bmsc=DC121B4952D3F7A44A37B58533205FDE~000000000000000000000000000000~YAAQN/vaFxNFrZ6HAQAA6aYpuxM7sqEs3gTRpF1tNkGVF3V/wFs9WboVUVxkpyC8p+Zx2dtb6gd698V0IqxIov3++CViewbFJydFZ1UrS2tuZF0WD0XcJ22pyL/n4nnl1rTbEYljujlHuKwTcJClHrwOPKG0tcD2eCdKeaoknSqZfMudyyoY5tdY/NYqz2KGED9idldzZ+WoWlBhJzKJ1tubQ9dlY5dp4UW8CsDKOwd6gGTGoYUq79iUWe5aBmmLHMCNg1F98H4Yf4hSwdjPcuF6VQusZQu4zpC0i5zPL/LzFCImVf1sja7HgUFvsnjme6utWgfhevvA6ZG7J6lRzGqki019U4stOmObn60zpuyEDD+NazzGiylQQi9f5oi/+OzZisgZuGD8bgAzyQNoaxdzpaV7qvFROj5/y2UyDeBrS95H+qdkZY+hA/5ElBfZW1rf5pnuseZRHW/OY3tAM9uAJ/IBFTOrf6HubrjcBkNiklcttLpwRbupe8JvlquhGhDnwlqCwFkCoTquWw7AM80BnoosLjKW/oymR6ZKfj1+Lcc=; wmlh=93c12d64600893e0507fa070dde1cafd1dc98def51c2b9fa76a755ba19b78e41; auth=MTAyOTYyMDE4uM5oBK9O%2BHyS1f9pkfboU87iS6YS8AKzZKJgXKxKU5gTUZuVpu5JhQlCpL2WTQTtCw82uWCJocKhH8n8EjQsvdYQ66ldbjS8gOPjmbyxHgh%2FjN2bLqy21PBHJyHIvowL767wuZloTfhm7Wk2Kcjygp0i2CSRVbB3L7ys%2FtvUzQcajUDufGunsD023vA3g3HyMRwN0dorTh%2BIUcmtKyTVtK9%2F3WZ19og1fnJXGgJCsB0UMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHQM1yzeYqcKuyBf7yiMsC3pKnKJ%2FqcX5sRloGT7yl1ZkNAw9vHcJPWhW8uWhTiUA8fsrp5wb3mJbHybVuzYEfLpNJiPaeVtf75KiMN%2B3ALhel6zVOjXcXpG6M%2FtZGGwUWkjyrOXbKKhH072NS%2FW0j%2FU%3D; _pxff_cfp=1; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyNjI3IiwiZGlzcGxheU5hbWUiOiJUYW1wYSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiIzMzYxMiIsImFkZHJlc3NMaW5lMSI6IjI3MDEgRSBGbGV0Y2hlciBBdmUiLCJjaXR5IjoiVGFtcGEiLCJzdGF0ZSI6IkZMIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiIzMzYxMi05NDE0In0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjoyOC4wNjgyNDMsImxvbmdpdHVkZSI6LTgyLjQyODE5NX0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImh1Yk5vZGVJZCI6IjI2MjciLCJzdG9yZUhycyI6IjA2OjAwLTIzOjAwIiwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiUElDS1VQX0NVUkJTSURFIiwiUElDS1VQX0lOU1RPUkUiXX1dLCJzaGlwcGluZ0FkZHJlc3MiOnsibGF0aXR1ZGUiOjI4LjA1NDYsImxvbmdpdHVkZSI6LTgyLjQxMTcsInBvc3RhbENvZGUiOiIzMzYyMCIsImNpdHkiOiJUYW1wYSIsInN0YXRlIjoiRkwiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjYyNyIsImRpc3BsYXlOYW1lIjoiVGFtcGEgU3VwZXJjZW50ZXIiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfQ1VSQlNJREUiLCJQSUNLVVBfSU5TVE9SRSJdLCJpbnRlbnQiOiJQSUNLVVAifSwiaW5zdG9yZSI6ZmFsc2UsImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMjYyNyIsImRpc3BsYXlOYW1lIjoiVGFtcGEgU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiMzM2MTIiLCJhZGRyZXNzTGluZTEiOiIyNzAxIEUgRmxldGNoZXIgQXZlIiwiY2l0eSI6IlRhbXBhIiwic3RhdGUiOiJGTCIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiMzM2MTItOTQxNCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MjguMDY4MjQzLCJsb25naXR1ZGUiOi04Mi40MjgxOTV9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyNjI3IiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwicmVmcmVzaEF0IjoxNjgyNDc0NDc2NjY4LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YzdiMzc1NTAtMTlkZi00OTFjLTk0ZTUtOWFhNmE3YjFhY2UwIn0%3D; AID=wmlspartner%3Dwmtlabs%3Areflectorid%3D22222222220220085369%3Alastupd%3D1682474225378; xptwj=rq:b2b4852f7c4c317e7168:XePPCGGMzonpGem0NpVdzQOQ1KrV8F8OorlJ5goO3HALzKGfFEQoNSp6vmBaQpbhQzSEd9/CrGdgPZh97bCp+n93s9J40o5wDjYFs08t0LcLSc3uTEYCLrkB; akavpau_p2=1682474826~id=d3a3f7bf5ec8f7a0f6376e14f2aab209; adblocked=true; _px3=46b136dafb9bd9af87581ebc1f12b1de00a451eb8f94196a38ee1af0c1c9c3ee:j3JiJv3fjaNWp0HOguvPzddfb5AzxEJ9GOTt+jg9ExRw79RLufL1uLW7S2xrb5qat6tRO5h76xWxuQiRT/+k4A==:1000:8RftyzZUY2ag7C5Rp3Frwpq+Xn7E38vxLTGCczfbplMbUIpxSBVrSiq2nzB9+rt1b6EJNUsiPDc1/Nx77dJiz9lyVLWTZy7lyE/oivqTCTBENw7ZZP+kkc8wAoMsx6wx7jcFAbyO+Uo/Lhlytlinq1Uf+SOXktnKYPgM4eIieuxZLsnH8FghupXVg3CsCq1XBGhXgQdMlgiywAOI3S5HyQ==; com.wm.reflector="reflectorid:22222222220220085369@lastupd:1682474231000@firstcreate:1682473413164"; xptwg=4268510774:19070469C68FC10:3FE3A1D:9DB27F4D:CDE778C6:72FD8008:; TS012768cf=013809551ac4688da31fa3964a69ee576e559433e667d3848dcf46f93c7de9064632d34508e28f2ff8db2a8396882e0bb93724e0f4; TS01a90220=013809551ac4688da31fa3964a69ee576e559433e667d3848dcf46f93c7de9064632d34508e28f2ff8db2a8396882e0bb93724e0f4; TS2a5e0c5c027=08882d7f05ab20005d56d385666dcb05627fbd227a7a988122455fa2dae1c913161787a82c083ec70829b93a7c1130005d77840d02b4ffc694f972c7ccc764b89ca03a2913b9a023ba86b541a84df2dcd7d0a208409d5124ba0bcf189da47fe4; _pxde=0053caf8aff259d88da46da8b0cf75fd7818e5977a8475a904fc275a289a19ab:eyJ0aW1lc3RhbXAiOjE2ODI0NzQyNjQwNTZ9; 23',
    'device_profile_ref_id': 'EmMUmJI5uN4G4WARUEi6vRhJp7ZmcGkWzn-_',
    'referer': 'https://www.walmart.com/browse/clothing/men/5438_133197?povid=ApparelNav_MENS_Mens_CP_LHN_Cat_MensShopAll&affinityOverride=default&page=2',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-83916c66d5d4d464abdea84a788aecd6-30d6f0e8973d431a-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'wm_mp': 'true',
    'wm_page_url': 'https://www.walmart.com/browse/clothing/men/5438_133197?povid=ApparelNav_MENS_Mens_CP_LHN_Cat_MensShopAll&affinityOverride=default&page=2',
    'wm_qos.correlation_id': 'MLw3W7t8GWPX1Yub8IBx9MadC-fhChVRiiNE',
    'x-apollo-operation-name': 'Browse',
    'x-enable-server-timing': '1',
    'x-latency-trace': '1',
    'x-o-bu': 'WALMART-US',
    'x-o-ccm': 'server',
    'x-o-correlation-id': 'MLw3W7t8GWPX1Yub8IBx9MadC-fhChVRiiNE',
    'x-o-gql-query': 'query Browse',
    'x-o-mart': 'B2C',
    'x-o-platform': 'rweb',
    'x-o-platform-version': 'main-1.65.1-535e56-0424T1046',
    'x-o-segment': 'oaoh'
}

# information on women clothing products
url_w = "https://www.walmart.com/orchestra/snb/graphql/Browse/d01009a483e647604f8f065494542e7f315990b079a7c2405505fc52b240712b/browse?variables=%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22default%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22%22%2C%22page%22%3A2%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%225438_133162%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22%22%2C%22cat_id%22%3A%225438_133162%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22default%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22%22%2C%22page%22%3A2%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%225438_133162%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22%22%2C%22cat_id%22%3A%225438_133162%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%225438_133162%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Afalse%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchSbaTop%22%3Afalse%2C%22fetchGallery%22%3Afalse%2C%22enablePortableFacets%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFacetCount%22%3Atrue%2C%22enableFlattenedFitment%22%3Atrue%2C%22enableMultiSave%22%3Afalse%2C%22pageType%22%3A%22BrowsePage%22%7D"
headers_w = {
    'authority': 'www.walmart.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'vtc=b0aBhLSilb0AwCYpa7JkR0; TBV=7; _pxvid=2b09f16e-e3c5-11ed-9a25-4579674d6a47; ACID=c7b37550-19df-491c-94e5-9aa6a7b1ace0; hasACID=true; abqme=false; _pxhd=eadf3282914f024dc829e1283f6e9973e6e0bd7f2061e15e6442c57e2455c6ab:2b08d268-e3c5-11ed-ac0c-56434d66556e; bstc=bFbLrIT4qCo3gXmmGnXMzk; auth=MTAyOTYyMDE4uM5oBK9O%2BHyS1f9pkfboU87iS6YS8AKzZKJgXKxKU5gTUZuVpu5JhQlCpL2WTQTtCw82uWCJocKhH8n8EjQsvdYQ66ldbjS8gOPjmbyxHgh%2FjN2bLqy21PBHJyHIvowL767wuZloTfhm7Wk2Kcjygi5k0VvBM%2FJjwcKWWhCnBS9z5wpY5aEbSaAt409Mp4ofoaZqmwCLpmv1E4ZyvWD69rZG0wfrK%2FK2otJ%2Fffz3x%2FgUMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHZzGahmQNK0p5WdJe7X4UhUBFoxWNBOtCgxx8q5%2F54ICQfWisvDJnUPeieBp0oqFeQeIHkJ%2BGdmZxh4qL3mRsJDeMY4lSM5cR0bA8xTd8qMIFzv%2BVv%2BhQdohPLt%2FTnsQ0kjyrOXbKKhH072NS%2FW0j%2FU%3D; assortmentStoreId=2627; hasLocData=1; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjI2MjciLCJ0aW1lc3RhbXAiOjE2ODI0NjcxNDg5MDR9LCJzaGlwcGluZ0FkZHJlc3MiOnsidGltZXN0YW1wIjoxNjgyNDY3MTQ4OTA0LCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6IjMzNjIwIiwiY2l0eSI6IlRhbXBhIiwic3RhdGUiOiJGTCIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiIyNjI3IiwidHlwZSI6IkRFTElWRVJZIiwic3RvcmVTZWxlY3Rpb25UeXBlIjpudWxsLCJzdG9yZVNlbGVjdGlvblNvdXJjZSI6bnVsbH1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE2ODI0NjcxNDg5MDQsImJhc2UiOiIzMzYyMCJ9LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YzdiMzc1NTAtMTlkZi00OTFjLTk0ZTUtOWFhNmE3YjFhY2UwIn0%3D; mobileweb=0; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=10hNA|2s5aC|5T7w_|6mVys|7AiHj|7ZWSr|8xsUp|ACUTJ|D8jju|Hsl6B|JHHZQ|K5ar6|M0qc8|No0Ca|Onkhp|PuiMD|Qhov8|RKlod|ULRlt|WB4Te|X78hm|YnYws|_4HRC|_9eqK|afTN6|btMCR|bvXlL|c8tN_|ce_CN|h-QLL|hA_Hz|jJAPh|jzyMV|k5HHI|kHCgj|kfniS|lPtmn|pWGxn|q8ZkB|tF78O|u5Y8n|vYtA6|xMGB0|z3-UY; exp-ck=10hNA15T7w_36mVys17AiHj17ZWSr1ACUTJ2D8jju1K5ar61ULRlt2YnYws4_9eqK1afTN62ce_CN1jJAPh2jzyMV1k5HHI1lPtmn1pWGxn1q8ZkB1tF78O1u5Y8n1vYtA61z3-UY2; xptc=assortmentStoreId%2B2627; xpm=1%2B1682484117%2Bb0aBhLSilb0AwCYpa7JkR0~%2B0; _astc=6e0f72e727ebf34ef1186c75b1438fd2; pxcts=06ec97da-e3ed-11ed-916c-4c74544e6e75; wmlh=93c12d64600893e0507fa070dde1cafd1dc98def51c2b9fa76a755ba19b78e41; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyNjI3IiwiZGlzcGxheU5hbWUiOiJUYW1wYSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiIzMzYxMiIsImFkZHJlc3NMaW5lMSI6IjI3MDEgRSBGbGV0Y2hlciBBdmUiLCJjaXR5IjoiVGFtcGEiLCJzdGF0ZSI6IkZMIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiIzMzYxMi05NDE0In0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjoyOC4wNjgyNDMsImxvbmdpdHVkZSI6LTgyLjQyODE5NX0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImh1Yk5vZGVJZCI6IjI2MjciLCJzdG9yZUhycyI6IjA2OjAwLTIzOjAwIiwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiUElDS1VQX0NVUkJTSURFIiwiUElDS1VQX0lOU1RPUkUiXX1dLCJzaGlwcGluZ0FkZHJlc3MiOnsibGF0aXR1ZGUiOjI4LjA1NDYsImxvbmdpdHVkZSI6LTgyLjQxMTcsInBvc3RhbENvZGUiOiIzMzYyMCIsImNpdHkiOiJUYW1wYSIsInN0YXRlIjoiRkwiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjYyNyIsImRpc3BsYXlOYW1lIjoiVGFtcGEgU3VwZXJjZW50ZXIiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfQ1VSQlNJREUiLCJQSUNLVVBfSU5TVE9SRSJdLCJpbnRlbnQiOiJQSUNLVVAifSwiaW5zdG9yZSI6ZmFsc2UsImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMjYyNyIsImRpc3BsYXlOYW1lIjoiVGFtcGEgU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiMzM2MTIiLCJhZGRyZXNzTGluZTEiOiIyNzAxIEUgRmxldGNoZXIgQXZlIiwiY2l0eSI6IlRhbXBhIiwic3RhdGUiOiJGTCIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiMzM2MTItOTQxNCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MjguMDY4MjQzLCJsb25naXR1ZGUiOi04Mi40MjgxOTV9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyNjI3IiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwicmVmcmVzaEF0IjoxNjgyNDg0OTgzOTM1LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YzdiMzc1NTAtMTlkZi00OTFjLTk0ZTUtOWFhNmE3YjFhY2UwIn0%3D; bm_mi=A5B2AC7FE6536A34EBA380BA5C0EAA3D~YAAQK/vaF1JxdKKHAQAA3OXmuxMaLaiOQ6SgGJGIKY2XIH+90RGrQXpd7vt3v0z/A1+ohdG6aIgSB9RnVrUVQCYkADDEiR9x5KOWFlHQKbmkLoZCORqUn2by3B2z7AXmga71WkMW1pC46pjDvFQ1D9lC6blGfvC5bXpuOYBk+nChNH4X2uiuYZ7JYxyULwpLO8iT9sG7sQ3EIW/bDHBR+5K5WABwaYnFP9R+Bk+RdJvTvNDHOtsKNPTUnHRpWEPwPAbFgl/kBJIXiOwDFFX9sU/fL8HQ0S5T9RZAdcIcnTO+udsD6r4WhrWOtb1BehCfxB7p9m//G+3scVWnrmZVQhFkyScDy0cSCcf0rWc=~1; _pxff_cfp=1; bm_sv=F7BBBB36632286389DC8647BA2915195~YAAQK/vaFx1zdKKHAQAANwznuxPquKZuuwDp9OiZ24eyLHQjAJwGViEY+KEXYlYYDRV8mcyXw3HXjqZTatT/wr0hU3f2jI4TV9NjKm5iR/uHVDhaqiGcZgJj+5202GDlSApHb/BNppC+Eoxb/2EqTdOF1HTz6xRf990N198pNFg8njtB3Q2DreI6Ihce6q8y9hy+YPZERIG/HufanxaM2NUnN/V6wKUcr24LHwz/cJ8XKCExrQ0iCnFM5umEA8YCFus=~1; AID=wmlspartner%3Dwmtlabs%3Areflectorid%3D22222222220220085369%3Alastupd%3D1682484705517; xptwj=rq:583e4de79d95553e29a6:Wd5gZPgyAWK5YNi9BX8nJP3i3EOiQi8DHj5GVfQX4xUjsPyqJogovAc8murUb75imkGwM1iGAi7wF/iKG1VIU1TY6ZLGVentmwRYyAVZVz06uXXEbCbmAMCQ9A==; akavpau_p2=1682485306~id=f513bcf55fa615d57e944ce38cbdfd9a; ak_bmsc=3E4E15F4DDB6299E9CED79623A792ECE~000000000000000000000000000000~YAAQK/vaF8J1dKKHAQAABjznuxOagZESjuTatcrGg27JxUYVoA+i2C+QcYIkRfZORdqdGB9PHmD6aC/nMYdOqt4OOhAnixerLtPzgUiQMoxvFwXJupi4i+2shbjyyiV9sfElWb8/w6jA29MKEGP45BEaFHZ9EbS3bXPTJ1dcDgz3xgzwlORT1ui0dE6FbQhTAOWSwVnKESsJA3SM0V/7DfgPpwkt82k/nZDik5RUIZSLoTGZ5g07lrnaYB6TIX3OxUEcNqUV4/lbWm6p4jcdI2TK/3fAir8o0BpO3S6DHK8h0I0qkXz3ZHToeOxwyJd4K6P63ZVkb15A2o80kSOgb71QNqBwT4+Yq1UP6UL7KSMG43VuIhDoLRfAGIjSqYqQvvfP7sVdozBV2oFp87FW0z6A8qmQns6DPJEqJ+OpEtQfyaSOyYGROt3UmHVW2xMrgE+ciU/q9tuaNPLWAbD5VtSo; adblocked=true; TS012768cf=0106cafa497e4bd41661b5229675b5cfe174c6e87ea81131270c410ddf6c72902c7d3a733141ebafaaa90e7d2326fa8ff4175e3300; TS01a90220=0106cafa497e4bd41661b5229675b5cfe174c6e87ea81131270c410ddf6c72902c7d3a733141ebafaaa90e7d2326fa8ff4175e3300; _px3=7221aa6705f8534514cdee01b4a1fb958976c6ae57ef9514c53ba32a7d039b4f:ultsPNPCyBCRaK+E6W7pLXW//FtrwmIipzBASW4sjkJ7tbjbiRPqrZZwmHwFLijOozd5FGfZGbIkCW2g2IHAsQ==:1000:Y7CbsUVOe5UO21nnW7Hjviodg/odSxWaIUGzbyLY6/FSAqBrtbwCsBBFJM7h06nV20V2eC2yyWZu0K87HJTRu4Pl9G1ZlD/n+dh+rNHqThdMQeHoh6IztkzkZ3z5gsXnND7D63zKyla40vp7slqTXczlxL6Fj/RsmlLnIgl12s4aJueGiiAWGLbPJfp3t8vH4dsnHGbBLHjIgRxlrGiv3Q==; _pxde=0c2bd56783873d4530c86f113055b9fdbf461e945c522778eb6c0c7d3cde8ede:eyJ0aW1lc3RhbXAiOjE2ODI0ODQ3MTIxMjJ9; com.wm.reflector="reflectorid:22222222220220085369@lastupd:1682484712000@firstcreate:1682473413164"; xptwg=3428198796:AB9C1A113171D0:1B613CA:DD5A2C8:342D0E4A:BE745F6E:; TS2a5e0c5c027=087a360d5eab200008febe516a8238d5ec8c0de7c14fa35dddee898012b7e184e1ad345e0db95a740860a59820113000ffd6868d9720dca834915e28b4c07de46ddc2ba79b46cd392c8dcd9b2e1d82f69ae98e8341c5919fb9c7b4890d9b2009; TS01a90220=01428e5934edbbb239034f039d52b39621d4ca7ef0ea4afc00f6efbb47c7f21fe272fa9deb04c03b17d610c02b08786a8f26fc3aef; bstc=bFbLrIT4qCo3gXmmGnXMzk; com.wm.reflector="reflectorid:22222222220220085369@lastupd:1682484767000@firstcreate:1682473413164"; exp-ck=10hNA15T7w_36mVys17AiHj17ZWSr1ACUTJ2D8jju1K5ar61ULRlt2YnYws4_9eqK1afTN62ce_CN1jJAPh2jzyMV1k5HHI1lPtmn1pWGxn1q8ZkB1tF78O1u5Y8n1vYtA61z3-UY2; mobileweb=0; vtc=b0aBhLSilb0AwCYpa7JkR0; xpa=10hNA|2s5aC|5T7w_|6mVys|7AiHj|7ZWSr|8xsUp|ACUTJ|D8jju|Hsl6B|JHHZQ|K5ar6|M0qc8|No0Ca|Onkhp|PuiMD|Qhov8|RKlod|ULRlt|WB4Te|X78hm|YnYws|_4HRC|_9eqK|afTN6|btMCR|bvXlL|c8tN_|ce_CN|h-QLL|hA_Hz|jJAPh|jzyMV|k5HHI|kHCgj|kfniS|lPtmn|pWGxn|q8ZkB|tF78O|u5Y8n|vYtA6|xMGB0|z3-UY; xpm=1%2B1682484117%2Bb0aBhLSilb0AwCYpa7JkR0~%2B0; xptc=assortmentStoreId%2B2627; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xptwg=2230955454:22712DDD1FECAA0:57EC13A:715B8A47:D84F5BA6:15A270E1:; TS012768cf=01428e5934edbbb239034f039d52b39621d4ca7ef0ea4afc00f6efbb47c7f21fe272fa9deb04c03b17d610c02b08786a8f26fc3aef; TS2a5e0c5c027=085414cdf8ab20000f0cbfacba8b0c07234c820ebbfc4bab97af434f0713dcf3a902522e78743869085d491198113000b37b4dca867ccfbe0f190cb3504925e7a9f01602a1c0cc18080b24c8dbb7834f8640554219fffbbfcd70fe4eaa959d7d; abqme=false; akavpau_p2=1682485367~id=9bc67e70125ef3bd03adf7dc79d49afb',
    'device_profile_ref_id': 'EmMUmJI5uN4G4WARUEi6vRhJp7ZmcGkWzn-_',
    'referer': 'https://www.walmart.com/browse/womens-clothing/5438_133162?povid=ApparelNav_WOMENS_WomensCPWomensClothing_CP_LHN_Cat_ShopAll&page=2&affinityOverride=default',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-ea823f6e78f1ba2dae426879884fea38-6fe3a33daf656638-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'wm_mp': 'true',
    'wm_page_url': 'https://www.walmart.com/browse/womens-clothing/5438_133162?povid=ApparelNav_WOMENS_WomensCPWomensClothing_CP_LHN_Cat_ShopAll&page=2&affinityOverride=default',
    'wm_qos.correlation_id': 'wqDEOFmzRzrne7s5Gmpjiv7rUHCrxelGItD3',
    'x-apollo-operation-name': 'Browse',
    'x-enable-server-timing': '1',
    'x-latency-trace': '1',
    'x-o-bu': 'WALMART-US',
    'x-o-ccm': 'server',
    'x-o-correlation-id': 'wqDEOFmzRzrne7s5Gmpjiv7rUHCrxelGItD3',
    'x-o-gql-query': 'query Browse',
    'x-o-mart': 'B2C',
    'x-o-platform': 'rweb',
    'x-o-platform-version': 'main-1.65.1-535e56-0424T1046',
    'x-o-segment': 'oaoh'
}

# information on boys clothing products
url_b = "https://www.walmart.com/orchestra/snb/graphql/Browse/d01009a483e647604f8f065494542e7f315990b079a7c2405505fc52b240712b/browse?variables=%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22default%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22%22%2C%22page%22%3A2%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%225438_7712430_7809949%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22%22%2C%22cat_id%22%3A%225438_7712430_7809949%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22default%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22%22%2C%22page%22%3A2%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%225438_7712430_7809949%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22%22%2C%22cat_id%22%3A%225438_7712430_7809949%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%225438_7712430_7809949%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Afalse%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchSbaTop%22%3Afalse%2C%22fetchGallery%22%3Afalse%2C%22enablePortableFacets%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFacetCount%22%3Atrue%2C%22enableFlattenedFitment%22%3Atrue%2C%22enableMultiSave%22%3Afalse%2C%22pageType%22%3A%22BrowsePage%22%7D"
headers_b = {
    'authority': 'www.walmart.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': 'vtc=b0aBhLSilb0AwCYpa7JkR0; TBV=7; _pxvid=2b09f16e-e3c5-11ed-9a25-4579674d6a47; ACID=c7b37550-19df-491c-94e5-9aa6a7b1ace0; hasACID=true; abqme=false; _pxhd=eadf3282914f024dc829e1283f6e9973e6e0bd7f2061e15e6442c57e2455c6ab:2b08d268-e3c5-11ed-ac0c-56434d66556e; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjI2MjciLCJ0aW1lc3RhbXAiOjE2ODI0NjcxNDg5MDR9LCJzaGlwcGluZ0FkZHJlc3MiOnsidGltZXN0YW1wIjoxNjgyNDY3MTQ4OTA0LCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6IjMzNjIwIiwiY2l0eSI6IlRhbXBhIiwic3RhdGUiOiJGTCIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiIyNjI3IiwidHlwZSI6IkRFTElWRVJZIiwic3RvcmVTZWxlY3Rpb25UeXBlIjpudWxsLCJzdG9yZVNlbGVjdGlvblNvdXJjZSI6bnVsbH1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE2ODI0NjcxNDg5MDQsImJhc2UiOiIzMzYyMCJ9LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YzdiMzc1NTAtMTlkZi00OTFjLTk0ZTUtOWFhNmE3YjFhY2UwIn0%3D; _astc=6e0f72e727ebf34ef1186c75b1438fd2; pxcts=06ec97da-e3ed-11ed-916c-4c74544e6e75; wmlh=93c12d64600893e0507fa070dde1cafd1dc98def51c2b9fa76a755ba19b78e41; bm_mi=A5B2AC7FE6536A34EBA380BA5C0EAA3D~YAAQK/vaF1JxdKKHAQAA3OXmuxMaLaiOQ6SgGJGIKY2XIH+90RGrQXpd7vt3v0z/A1+ohdG6aIgSB9RnVrUVQCYkADDEiR9x5KOWFlHQKbmkLoZCORqUn2by3B2z7AXmga71WkMW1pC46pjDvFQ1D9lC6blGfvC5bXpuOYBk+nChNH4X2uiuYZ7JYxyULwpLO8iT9sG7sQ3EIW/bDHBR+5K5WABwaYnFP9R+Bk+RdJvTvNDHOtsKNPTUnHRpWEPwPAbFgl/kBJIXiOwDFFX9sU/fL8HQ0S5T9RZAdcIcnTO+udsD6r4WhrWOtb1BehCfxB7p9m//G+3scVWnrmZVQhFkyScDy0cSCcf0rWc=~1; bm_sv=F7BBBB36632286389DC8647BA2915195~YAAQK/vaFx1zdKKHAQAANwznuxPquKZuuwDp9OiZ24eyLHQjAJwGViEY+KEXYlYYDRV8mcyXw3HXjqZTatT/wr0hU3f2jI4TV9NjKm5iR/uHVDhaqiGcZgJj+5202GDlSApHb/BNppC+Eoxb/2EqTdOF1HTz6xRf990N198pNFg8njtB3Q2DreI6Ihce6q8y9hy+YPZERIG/HufanxaM2NUnN/V6wKUcr24LHwz/cJ8XKCExrQ0iCnFM5umEA8YCFus=~1; ak_bmsc=3E4E15F4DDB6299E9CED79623A792ECE~000000000000000000000000000000~YAAQK/vaF8J1dKKHAQAABjznuxOagZESjuTatcrGg27JxUYVoA+i2C+QcYIkRfZORdqdGB9PHmD6aC/nMYdOqt4OOhAnixerLtPzgUiQMoxvFwXJupi4i+2shbjyyiV9sfElWb8/w6jA29MKEGP45BEaFHZ9EbS3bXPTJ1dcDgz3xgzwlORT1ui0dE6FbQhTAOWSwVnKESsJA3SM0V/7DfgPpwkt82k/nZDik5RUIZSLoTGZ5g07lrnaYB6TIX3OxUEcNqUV4/lbWm6p4jcdI2TK/3fAir8o0BpO3S6DHK8h0I0qkXz3ZHToeOxwyJd4K6P63ZVkb15A2o80kSOgb71QNqBwT4+Yq1UP6UL7KSMG43VuIhDoLRfAGIjSqYqQvvfP7sVdozBV2oFp87FW0z6A8qmQns6DPJEqJ+OpEtQfyaSOyYGROt3UmHVW2xMrgE+ciU/q9tuaNPLWAbD5VtSo; bstc=YRfjURj_uc3bHN0Ic8LR7M; mobileweb=0; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=10hNA|2s5aC|5T7w_|6mVys|7AiHj|7ZWSr|8xsUp|ACUTJ|D8jju|Hsl6B|JHHZQ|K5ar6|M0qc8|No0Ca|Onkhp|PuiMD|Qhov8|RKlod|ULRlt|WB4Te|X78hm|YnYws|_4HRC|_9eqK|afTN6|btMCR|bvXlL|c8tN_|ce_CN|h-QLL|hA_Hz|jJAPh|jzyMV|k5HHI|kHCgj|kfniS|lPtmn|pWGxn|q8ZkB|tF78O|u5Y8n|vYtA6|xMGB0|z3-UY; exp-ck=10hNA15T7w_36mVys17AiHj17ZWSr1ACUTJ2D8jju1K5ar61ULRlt2YnYws4_9eqK1afTN62ce_CN1jJAPh2jzyMV1k5HHI1lPtmn1pWGxn1q8ZkB1tF78O1u5Y8n1vYtA61z3-UY2; auth=MTAyOTYyMDE4uM5oBK9O%2BHyS1f9pkfboU87iS6YS8AKzZKJgXKxKU5gTUZuVpu5JhQlCpL2WTQTtCw82uWCJocKhH8n8EjQsvdYQ66ldbjS8gOPjmbyxHgh%2FjN2bLqy21PBHJyHIvowL767wuZloTfhm7Wk2KcjygpySosImygUk1x1iKsdnk4%2BxImEs17pwPY3wDEHLekiPLZUaoYJJ33emtjD4s%2BfIMz2YRjVPhANsDhXIeu%2FX3JUUMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHXfhgPAe1kxGH7Y4aaIztzsePs6fP%2Fc97bPx5KLnDgtHh1XDEMw%2FdjW2VBuBEKaaXD6ewtW0Cox0Ue%2BTrElUFig3hwTorKaKZndSCSupnmQBw8y4waT0sOOCGfpSwKYYaJE5WBBdZBCyKnCQAR7o6eg%3D; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyNjI3IiwiZGlzcGxheU5hbWUiOiJUYW1wYSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiIzMzYxMiIsImFkZHJlc3NMaW5lMSI6IjI3MDEgRSBGbGV0Y2hlciBBdmUiLCJjaXR5IjoiVGFtcGEiLCJzdGF0ZSI6IkZMIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiIzMzYxMi05NDE0In0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjoyOC4wNjgyNDMsImxvbmdpdHVkZSI6LTgyLjQyODE5NX0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImh1Yk5vZGVJZCI6IjI2MjciLCJzdG9yZUhycyI6IjA2OjAwLTIzOjAwIiwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiUElDS1VQX0NVUkJTSURFIiwiUElDS1VQX0lOU1RPUkUiXX1dLCJzaGlwcGluZ0FkZHJlc3MiOnsibGF0aXR1ZGUiOjI4LjA1NDYsImxvbmdpdHVkZSI6LTgyLjQxMTcsInBvc3RhbENvZGUiOiIzMzYyMCIsImNpdHkiOiJUYW1wYSIsInN0YXRlIjoiRkwiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjYyNyIsImRpc3BsYXlOYW1lIjoiVGFtcGEgU3VwZXJjZW50ZXIiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfQ1VSQlNJREUiLCJQSUNLVVBfSU5TVE9SRSJdLCJpbnRlbnQiOiJQSUNLVVAifSwiaW5zdG9yZSI6ZmFsc2UsImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMjYyNyIsImRpc3BsYXlOYW1lIjoiVGFtcGEgU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiMzM2MTIiLCJhZGRyZXNzTGluZTEiOiIyNzAxIEUgRmxldGNoZXIgQXZlIiwiY2l0eSI6IlRhbXBhIiwic3RhdGUiOiJGTCIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiMzM2MTItOTQxNCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MjguMDY4MjQzLCJsb25naXR1ZGUiOi04Mi40MjgxOTV9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyNjI3IiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwicmVmcmVzaEF0IjoxNjgyNDkxMDI3NjUzLCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YzdiMzc1NTAtMTlkZi00OTFjLTk0ZTUtOWFhNmE3YjFhY2UwIn0%3D; assortmentStoreId=2627; hasLocData=1; xptc=assortmentStoreId%2B2627; xpm=1%2B1682490728%2Bb0aBhLSilb0AwCYpa7JkR0~%2B0; _pxff_cfp=1; AID=wmlspartner%3Dwmtlabs%3Areflectorid%3D22222222220220085369%3Alastupd%3D1682490860086; xptwj=rq:4b7840ca946402a41ae2:41gcoOXVyIvlEbWa9IS1dBhiTHu4I1u2STNG1Kp/qU0+KQjPbTWJ2jcwiYF0E1fxmKzWmyYOhJRI9XKSVtDrCKu2KApja7VklOd/cSFUFXG8l9lDuvhrTA/KQA==; akavpau_p2=1682491461~id=dacccfb6007a9c954ac6287251d87303; adblocked=true; _px3=e8766a404f8c7010ef0d2077de41b5a709fe33be970dcff44435b8d461974b7d:ThNGETmSJefu5gxVGb7Vg7dwofKBtYGV1HaUHR9lNdLTCjOUgWAjHei3snyeyRY4Dn2WLKKBQuMoJrwB7yx4yw==:1000:3t9MHk+qiyX3YUpQibzeDMdg0fYtBpiSqbN0SVdCQQiIJBoTYFaCOG/xE72QLcmvTYaL3AU9aWctRLzcilzaRG01nalgp8YlCF4Hc/wWR0SqoUJCd/Q9HIDh0QrNOnWcctui4DLwThv2LzRkyE3/M77z3o680j6OWHimvQMVGP/uF8kkTmwjcD9Apbt/5L3WhQzs+JcBBszuWsHeyQkQHw==; com.wm.reflector="reflectorid:22222222220220085369@lastupd:1682490866000@firstcreate:1682473413164"; xptwg=2260559195:23F4583259A78E0:5BC8543:B33C2BB5:810587CF:54B91A8B:; TS012768cf=0136a0061ea3be54c39d44ebe7d33d4741c3e8729dc68a66fa50d8012e40b91e00c26b3319b3f97e1c1318df50722e75a7b0d38117; TS01a90220=0136a0061ea3be54c39d44ebe7d33d4741c3e8729dc68a66fa50d8012e40b91e00c26b3319b3f97e1c1318df50722e75a7b0d38117; TS2a5e0c5c027=08cf765f65ab20003ebbe5e887b606d303c55c1092c5742aba128d1cfa778d23d0589d7599a58be608d0b64a1111300040db088c332dbdf0437437bc11b55cbf5637dad09de50d7a00a3e81afbff4dc79dc63d663ac608df0e57d1e2d9ab25d5; _pxde=565323a43f5e548be2337713d19ff84d69ac8e2738ae29153750732d1461b4f7:eyJ0aW1lc3RhbXAiOjE2ODI0OTA4NzA3OTh9; 22; TS01a90220=01428e5934edbbb239034f039d52b39621d4ca7ef0ea4afc00f6efbb47c7f21fe272fa9deb04c03b17d610c02b08786a8f26fc3aef; com.wm.reflector="reflectorid:22222222220220085369@lastupd:1682484767000@firstcreate:1682473413164"; vtc=b0aBhLSilb0AwCYpa7JkR0; xptwg=2230955454:22712DDD1FECAA0:57EC13A:715B8A47:D84F5BA6:15A270E1:; TS012768cf=01428e5934edbbb239034f039d52b39621d4ca7ef0ea4afc00f6efbb47c7f21fe272fa9deb04c03b17d610c02b08786a8f26fc3aef; TS2a5e0c5c027=085414cdf8ab20000f0cbfacba8b0c07234c820ebbfc4bab97af434f0713dcf3a902522e78743869085d491198113000b37b4dca867ccfbe0f190cb3504925e7a9f01602a1c0cc18080b24c8dbb7834f8640554219fffbbfcd70fe4eaa959d7d; abqme=false; akavpau_p2=1682485367~id=9bc67e70125ef3bd03adf7dc79d49afb',
    'device_profile_ref_id': 'EmMUmJI5uN4G4WARUEi6vRhJp7ZmcGkWzn-_',
    'referer': 'https://www.walmart.com/browse/clothing/boys-clothing/5438_7712430_7809949?povid=FashionTopNav_Kids_Boys_Clothing_All&page=2&affinityOverride=default',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-9b61218b3477a825d4de49df6e710d07-f4406717eba42bd7-00',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'wm_mp': 'true',
    'wm_page_url': 'https://www.walmart.com/browse/clothing/boys-clothing/5438_7712430_7809949?povid=FashionTopNav_Kids_Boys_Clothing_All&page=2&affinityOverride=default',
    'wm_qos.correlation_id': '0doblpiE_3nLQfRhlo_1gwnNKPXEpUYj6NJL',
    'x-apollo-operation-name': 'Browse',
    'x-enable-server-timing': '1',
    'x-latency-trace': '1',
    'x-o-bu': 'WALMART-US',
    'x-o-ccm': 'server',
    'x-o-correlation-id': '0doblpiE_3nLQfRhlo_1gwnNKPXEpUYj6NJL',
    'x-o-gql-query': 'query Browse',
    'x-o-mart': 'B2C',
    'x-o-platform': 'rweb',
    'x-o-platform-version': 'main-1.66.0-1ebba6-0425T2118',
    'x-o-segment': 'oaoh'
}

# information on girls clothing products
url_g = "https://www.walmart.com/orchestra/snb/graphql/Browse/d01009a483e647604f8f065494542e7f315990b079a7c2405505fc52b240712b/browse?variables=%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22default%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22%22%2C%22page%22%3A2%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%225438_7712430_1660851%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22%22%2C%22cat_id%22%3A%225438_7712430_1660851%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22fitmentFieldParams%22%3A%7B%22powerSportEnabled%22%3Atrue%7D%2C%22fitmentSearchParams%22%3A%7B%22id%22%3A%22%22%2C%22affinityOverride%22%3A%22default%22%2C%22dealsId%22%3A%22%22%2C%22query%22%3A%22%22%2C%22page%22%3A2%2C%22prg%22%3A%22desktop%22%2C%22catId%22%3A%225438_7712430_1660851%22%2C%22facet%22%3A%22%22%2C%22sort%22%3A%22best_match%22%2C%22rawFacet%22%3A%22%22%2C%22seoPath%22%3A%22%22%2C%22ps%22%3A40%2C%22ptss%22%3A%22%22%2C%22trsp%22%3A%22%22%2C%22beShelfId%22%3A%22%22%2C%22recall_set%22%3A%22%22%2C%22module_search%22%3A%22%22%2C%22min_price%22%3A%22%22%2C%22max_price%22%3A%22%22%2C%22storeSlotBooked%22%3A%22%22%2C%22additionalQueryParams%22%3A%7B%22hidden_facet%22%3Anull%2C%22translation%22%3Anull%2C%22isMoreOptionsTileEnabled%22%3Atrue%7D%2C%22searchArgs%22%3A%7B%22query%22%3A%22%22%2C%22cat_id%22%3A%225438_7712430_1660851%22%2C%22prg%22%3A%22desktop%22%2C%22facet%22%3A%22%22%7D%2C%22cat_id%22%3A%225438_7712430_1660851%22%2C%22_be_shelf_id%22%3A%22%22%7D%2C%22enableFashionTopNav%22%3Afalse%2C%22fetchMarquee%22%3Atrue%2C%22fetchSkyline%22%3Atrue%2C%22fetchSbaTop%22%3Afalse%2C%22fetchGallery%22%3Afalse%2C%22enablePortableFacets%22%3Atrue%2C%22tenant%22%3A%22WM_GLASS%22%2C%22enableFacetCount%22%3Atrue%2C%22enableFlattenedFitment%22%3Atrue%2C%22enableMultiSave%22%3Afalse%2C%22pageType%22%3A%22BrowsePage%22%7D"
headers_g = {
  'authority': 'www.walmart.com',
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': 'vtc=b0aBhLSilb0AwCYpa7JkR0; TBV=7; _pxvid=2b09f16e-e3c5-11ed-9a25-4579674d6a47; ACID=c7b37550-19df-491c-94e5-9aa6a7b1ace0; hasACID=true; abqme=false; _pxhd=eadf3282914f024dc829e1283f6e9973e6e0bd7f2061e15e6442c57e2455c6ab:2b08d268-e3c5-11ed-ac0c-56434d66556e; locGuestData=eyJpbnRlbnQiOiJTSElQUElORyIsImlzRXhwbGljaXQiOmZhbHNlLCJzdG9yZUludGVudCI6IlBJQ0tVUCIsIm1lcmdlRmxhZyI6ZmFsc2UsImlzRGVmYXVsdGVkIjpmYWxzZSwicGlja3VwIjp7Im5vZGVJZCI6IjI2MjciLCJ0aW1lc3RhbXAiOjE2ODI0NjcxNDg5MDR9LCJzaGlwcGluZ0FkZHJlc3MiOnsidGltZXN0YW1wIjoxNjgyNDY3MTQ4OTA0LCJ0eXBlIjoicGFydGlhbC1sb2NhdGlvbiIsImdpZnRBZGRyZXNzIjpmYWxzZSwicG9zdGFsQ29kZSI6IjMzNjIwIiwiY2l0eSI6IlRhbXBhIiwic3RhdGUiOiJGTCIsImRlbGl2ZXJ5U3RvcmVMaXN0IjpbeyJub2RlSWQiOiIyNjI3IiwidHlwZSI6IkRFTElWRVJZIiwic3RvcmVTZWxlY3Rpb25UeXBlIjpudWxsLCJzdG9yZVNlbGVjdGlvblNvdXJjZSI6bnVsbH1dfSwicG9zdGFsQ29kZSI6eyJ0aW1lc3RhbXAiOjE2ODI0NjcxNDg5MDQsImJhc2UiOiIzMzYyMCJ9LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YzdiMzc1NTAtMTlkZi00OTFjLTk0ZTUtOWFhNmE3YjFhY2UwIn0%3D; _astc=6e0f72e727ebf34ef1186c75b1438fd2; pxcts=06ec97da-e3ed-11ed-916c-4c74544e6e75; wmlh=93c12d64600893e0507fa070dde1cafd1dc98def51c2b9fa76a755ba19b78e41; bstc=YRfjURj_uc3bHN0Ic8LR7M; mobileweb=0; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xpa=10hNA|2s5aC|5T7w_|6mVys|7AiHj|7ZWSr|8xsUp|ACUTJ|D8jju|Hsl6B|JHHZQ|K5ar6|M0qc8|No0Ca|Onkhp|PuiMD|Qhov8|RKlod|ULRlt|WB4Te|X78hm|YnYws|_4HRC|_9eqK|afTN6|btMCR|bvXlL|c8tN_|ce_CN|h-QLL|hA_Hz|jJAPh|jzyMV|k5HHI|kHCgj|kfniS|lPtmn|pWGxn|q8ZkB|tF78O|u5Y8n|vYtA6|xMGB0|z3-UY; exp-ck=10hNA15T7w_36mVys17AiHj17ZWSr1ACUTJ2D8jju1K5ar61ULRlt2YnYws4_9eqK1afTN62ce_CN1jJAPh2jzyMV1k5HHI1lPtmn1pWGxn1q8ZkB1tF78O1u5Y8n1vYtA61z3-UY2; auth=MTAyOTYyMDE4uM5oBK9O%2BHyS1f9pkfboU87iS6YS8AKzZKJgXKxKU5gTUZuVpu5JhQlCpL2WTQTtCw82uWCJocKhH8n8EjQsvdYQ66ldbjS8gOPjmbyxHgh%2FjN2bLqy21PBHJyHIvowL767wuZloTfhm7Wk2KcjygpySosImygUk1x1iKsdnk4%2BxImEs17pwPY3wDEHLekiPLZUaoYJJ33emtjD4s%2BfIMz2YRjVPhANsDhXIeu%2FX3JUUMk70P8glgOEpLOprhDfMDCcb9mgycy9jtT1uIyOBHXfhgPAe1kxGH7Y4aaIztzsePs6fP%2Fc97bPx5KLnDgtHh1XDEMw%2FdjW2VBuBEKaaXD6ewtW0Cox0Ue%2BTrElUFig3hwTorKaKZndSCSupnmQBw8y4waT0sOOCGfpSwKYYaJE5WBBdZBCyKnCQAR7o6eg%3D; assortmentStoreId=2627; hasLocData=1; xptc=assortmentStoreId%2B2627; xpm=1%2B1682490728%2Bb0aBhLSilb0AwCYpa7JkR0~%2B0; ak_bmsc=EA9A3CA792FF48BF693B0D975B7CC8F2~000000000000000000000000000000~YAAQN/vaF+3es56HAQAAgh9MvBNXNAisc9jMbS6J1j/K+GKBfhGxFiBV84f+5hHmcDwsLAT20bvb7DiBVLgnSdIWBjQKPvKceWLBb+4HRTnGfeUMy121YiyTsyT7h/+7LnnF95lOEXX28+HPtJzNFznDWjx92yRbc9/AyaGV/51IzseUldprBIVIDmird2nZCuDWbPPKjYiNjClU+MxIQhJVEgNrP+MQVe/cTACBq4IlCQFioz1KJwSdQR/+UVN1KgVF1JN2KOdu8wqTjsLEAAqIMf++mbEDSWIljXZ+AZbxxKQDcHfoiRUxlWBCqS21ytml7YE8lyvPtUVRWeGgUrUt8lj6ukDwd6mBZJd8o+ZuJ7Yava1kvDjlc4LhKtMCw1/amYwdZv0EyNbE; locDataV3=eyJpc0RlZmF1bHRlZCI6ZmFsc2UsImlzRXhwbGljaXQiOmZhbHNlLCJpbnRlbnQiOiJTSElQUElORyIsInBpY2t1cCI6W3siYnVJZCI6IjAiLCJub2RlSWQiOiIyNjI3IiwiZGlzcGxheU5hbWUiOiJUYW1wYSBTdXBlcmNlbnRlciIsIm5vZGVUeXBlIjoiU1RPUkUiLCJhZGRyZXNzIjp7InBvc3RhbENvZGUiOiIzMzYxMiIsImFkZHJlc3NMaW5lMSI6IjI3MDEgRSBGbGV0Y2hlciBBdmUiLCJjaXR5IjoiVGFtcGEiLCJzdGF0ZSI6IkZMIiwiY291bnRyeSI6IlVTIiwicG9zdGFsQ29kZTkiOiIzMzYxMi05NDE0In0sImdlb1BvaW50Ijp7ImxhdGl0dWRlIjoyOC4wNjgyNDMsImxvbmdpdHVkZSI6LTgyLjQyODE5NX0sImlzR2xhc3NFbmFibGVkIjp0cnVlLCJzY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJ1blNjaGVkdWxlZEVuYWJsZWQiOnRydWUsImh1Yk5vZGVJZCI6IjI2MjciLCJzdG9yZUhycyI6IjA2OjAwLTIzOjAwIiwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiUElDS1VQX0NVUkJTSURFIiwiUElDS1VQX0lOU1RPUkUiXX1dLCJzaGlwcGluZ0FkZHJlc3MiOnsibGF0aXR1ZGUiOjI4LjA1NDYsImxvbmdpdHVkZSI6LTgyLjQxMTcsInBvc3RhbENvZGUiOiIzMzYyMCIsImNpdHkiOiJUYW1wYSIsInN0YXRlIjoiRkwiLCJjb3VudHJ5Q29kZSI6IlVTQSIsImdpZnRBZGRyZXNzIjpmYWxzZX0sImFzc29ydG1lbnQiOnsibm9kZUlkIjoiMjYyNyIsImRpc3BsYXlOYW1lIjoiVGFtcGEgU3VwZXJjZW50ZXIiLCJzdXBwb3J0ZWRBY2Nlc3NUeXBlcyI6WyJQSUNLVVBfQ1VSQlNJREUiLCJQSUNLVVBfSU5TVE9SRSJdLCJpbnRlbnQiOiJQSUNLVVAifSwiaW5zdG9yZSI6ZmFsc2UsImRlbGl2ZXJ5Ijp7ImJ1SWQiOiIwIiwibm9kZUlkIjoiMjYyNyIsImRpc3BsYXlOYW1lIjoiVGFtcGEgU3VwZXJjZW50ZXIiLCJub2RlVHlwZSI6IlNUT1JFIiwiYWRkcmVzcyI6eyJwb3N0YWxDb2RlIjoiMzM2MTIiLCJhZGRyZXNzTGluZTEiOiIyNzAxIEUgRmxldGNoZXIgQXZlIiwiY2l0eSI6IlRhbXBhIiwic3RhdGUiOiJGTCIsImNvdW50cnkiOiJVUyIsInBvc3RhbENvZGU5IjoiMzM2MTItOTQxNCJ9LCJnZW9Qb2ludCI6eyJsYXRpdHVkZSI6MjguMDY4MjQzLCJsb25naXR1ZGUiOi04Mi40MjgxOTV9LCJpc0dsYXNzRW5hYmxlZCI6dHJ1ZSwic2NoZWR1bGVkRW5hYmxlZCI6dHJ1ZSwidW5TY2hlZHVsZWRFbmFibGVkIjp0cnVlLCJhY2Nlc3NQb2ludHMiOlt7ImFjY2Vzc1R5cGUiOiJERUxJVkVSWV9BRERSRVNTIn1dLCJodWJOb2RlSWQiOiIyNjI3IiwiaXNFeHByZXNzRGVsaXZlcnlPbmx5IjpmYWxzZSwic3VwcG9ydGVkQWNjZXNzVHlwZXMiOlsiREVMSVZFUllfQUREUkVTUyJdfSwicmVmcmVzaEF0IjoxNjgyNDkxNjQ3Njg3LCJ2YWxpZGF0ZUtleSI6InByb2Q6djI6YzdiMzc1NTAtMTlkZi00OTFjLTk0ZTUtOWFhNmE3YjFhY2UwIn0%3D; _pxff_cfp=1; AID=wmlspartner%3Dwmtlabs%3Areflectorid%3D22222222220220085369%3Alastupd%3D1682491383999; xptwj=rq:a6d3009d2be8c9fc030d:C5lScc5F6qKs0rkteFa4IOv2N18G2Q95zTP+xI65Gp7hAc7gUsZU9m/5OaORL2DLf+xEJOhXEB90yasa+EjkfAYKqGi0GoujbPxDu7137G0Cm0jAxcZyVF5SiA==; akavpau_p2=1682491984~id=682b9b382583488d4d74ea9ae97e6cfc; bm_mi=C7909CD884513D8D25E6E03B8901F98E~YAAQN/vaF/Xgs56HAQAAUSNNvBPkHB6nIEZWCguctr6uHjnF2NiTEAL2jI7ARDzahs0hH7MMvJ73M4KGrL6tlQEneN64Rb7hq0PUY5rqO/Fej52y8jxJAwddRARwaD90ERklFDkrHf116gCfy/W/qE2eThQ/2X2PXaBpxjWpHSV66jCwR78osktAbG/aF1d0AexjkiTuQqaiBnYJQHLFwtkgvfF3rYyXEzfg5vQIMWU5HEAIYJVdn5AsSQ7TdpRABC4Chcka/BiqIAp0a48aCmjve85MkkfEAzaTx6fnYBLIsKys1wzGOfRFUxj+ytis315KgpAMbuTGE0W1VVzLleSZ2J7Vql3XX3Rgk7nwCN20i6cunz0hrQhL1yGPlz4=~1; adblocked=true; _px3=7cd6dfa5497c8b4ca38c4e0984ed03b42874f846c2a6dad1c3421c257e3283f3:Yf/Y9UzJuFsfGYGsCEi5wOvCporhyvaNEpmik3XrriDBrZAOLiwwlYYX33Gbmth6OL5xFaHedBYg5UVEEEHlPQ==:1000:P7raUwKfsrDFGaGPISUyvxNNnUhMuN3okdJb2YgBh17Bw13VbpIUH7Z/dzt7LvnmAPO7EsdG9BRnE6TSgaUDokJzMcoyczHRwUKLDk5efUzmWdA02YV3PxDBIXyR4oCX0Dv2eL9H+UxgyIhR+NX+kcGzpPclodmzrXoonzPA/ieLHR9vzMOfCQyrgBEPwbOE0DscZ8MQbNIR8CSbxPNDvw==; com.wm.reflector="reflectorid:22222222220220085369@lastupd:1682491386000@firstcreate:1682473413164"; xptwg=2854256950:18FF0856BAA6F00:3FCF152:A8388882:EE3FE117:F5FD697:; TS012768cf=0141e2a088f4e246006ddc3a01831e0bb2a5a4e9917f8404ab9edfc089e06519756c88e34ce45213fa7c8a0fff741a07a215866384; TS01a90220=0141e2a088f4e246006ddc3a01831e0bb2a5a4e9917f8404ab9edfc089e06519756c88e34ce45213fa7c8a0fff741a07a215866384; TS2a5e0c5c027=087e4d6c1dab200072937eb9e94efc7e6a9fffa2d59e6c8f7bf7863379d1df5847d57b486b1fea0008996ff3a911300079c5e25b43b62b2dfd94f423353f97113f3b905a516691e081f07f5aba0ca007fce9667cd2a9c3c16839c430f52e6ce3; bm_sv=4E818468CBC7140EC5897B1F42691EFB~YAAQN/vaFwjhs56HAQAAditNvBOKFJpM3q7iPor9jZWxU1KR8uyGndqq59sl1FGzXyZudo4svQ2IqF6LWhBOtP3aTa5nZ7LTTGlniJ9icWI3PbiwPBDEciI7GXolr463/Frl2c/0mZ67v0OdTy4u8tR5Iqja4r919SdrkE57zD8MFA+S/GLgvH9r8IJwYxFGUI1k/w2ciGWk0/9bIL9AZOdLXCahJG5WXHxdbrXcsrwH0BSmvZ642paL5BtD5Y1j0Zw=~1; _pxde=68f5eecec0e479e396df995595e4b1ca3065cd00f52c54d3aeaa16ba888b724c:eyJ0aW1lc3RhbXAiOjE2ODI0OTEzOTA4MTJ9; 22; TS01a90220=0195e632c745d617aa74c48ef5a62cb6bd97ebc51a48246d0ed354a51e132002bed398e4a05544b0f627ba7a8c7fe500e0a24af1f2; bm_sv=4E818468CBC7140EC5897B1F42691EFB~YAAQkWjcFyqpt6eHAQAAlptNvBN0S3HfIybpdk4Yerr3s5o2OCDrY8zO06m4SxLJ0w4jWn6T8Ys3Z379/BRVEmUCFfbWKd/3XTVoD0wYvjUNQJhVZQuXCo42rXJxPdvkg3lBSmgmh+h+gSmkMcCTduZQN4rCqqGHsMm9e2b/nggECnnpC+MjbnmzQjm6fYjem8/znA4UBwkMirwayM4huOjNAQ7bHYN44wYsfY4b8dnIrLesdubX9tklS3kc766i5VQ=~1; bstc=YRfjURj_uc3bHN0Ic8LR7M; com.wm.reflector="reflectorid:22222222220220085369@lastupd:1682491415000@firstcreate:1682473413164"; exp-ck=10hNA15T7w_36mVys17AiHj17ZWSr1ACUTJ2D8jju1K5ar61ULRlt2YnYws4_9eqK1afTN62ce_CN1jJAPh2jzyMV1k5HHI1lPtmn1pWGxn1q8ZkB1tF78O1u5Y8n1vYtA61z3-UY2; mobileweb=0; vtc=b0aBhLSilb0AwCYpa7JkR0; xpa=10hNA|2s5aC|5T7w_|6mVys|7AiHj|7ZWSr|8xsUp|ACUTJ|D8jju|Hsl6B|JHHZQ|K5ar6|M0qc8|No0Ca|Onkhp|PuiMD|Qhov8|RKlod|ULRlt|WB4Te|X78hm|YnYws|_4HRC|_9eqK|afTN6|btMCR|bvXlL|c8tN_|ce_CN|h-QLL|hA_Hz|jJAPh|jzyMV|k5HHI|kHCgj|kfniS|lPtmn|pWGxn|q8ZkB|tF78O|u5Y8n|vYtA6|xMGB0|z3-UY; xpm=1%2B1682490728%2Bb0aBhLSilb0AwCYpa7JkR0~%2B0; xptc=assortmentStoreId%2B2627; xpth=x-o-mart%2BB2C~x-o-mverified%2Bfalse; xptwg=1305457192:10635DF07C7AF10:29D5B10:6746FA16:F75DCC03:8E8BF4CF:; TS012768cf=0195e632c745d617aa74c48ef5a62cb6bd97ebc51a48246d0ed354a51e132002bed398e4a05544b0f627ba7a8c7fe500e0a24af1f2; TS2a5e0c5c027=08f46d25a0ab2000a8faa31e509c61e15ca6932a22ff617ea701a2cc7713743aeec15519a949221b089513bc7711300046a7e5e8e9bc1d18aca30f24a825fa7d89457ecb960e21d336c6c5eb7bcac940c1d174191ca94bba41dfd889f6380dd7; abqme=false; akavpau_p2=1682492015~id=641f3cf624345152d473c94ae8cd75d6',
  'device_profile_ref_id': 'EmMUmJI5uN4G4WARUEi6vRhJp7ZmcGkWzn-_',
  'referer': 'https://www.walmart.com/browse/clothing/girls-clothing/5438_7712430_1660851?povid=FashionTopNav_Kids_Girls_Clothing_All&page=2&affinityOverride=default',
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'traceparent': '00-2b301622c1e95b2a3607de6f0e0bd53c-642501d929f10017-00',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'wm_mp': 'true',
  'wm_page_url': 'https://www.walmart.com/browse/clothing/girls-clothing/5438_7712430_1660851?povid=FashionTopNav_Kids_Girls_Clothing_All&page=2&affinityOverride=default',
  'wm_qos.correlation_id': 'VWDw_BmjPc6Jd_u3HQJ3Bv0NSVPQe01i02U5',
  'x-apollo-operation-name': 'Browse',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-US',
  'x-o-ccm': 'server',
  'x-o-correlation-id': 'VWDw_BmjPc6Jd_u3HQJ3Bv0NSVPQe01i02U5',
  'x-o-gql-query': 'query Browse',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-1.66.0-1ebba6-0425T2118',
  'x-o-segment': 'oaoh'
}

products = []

# removes quotes at beginning and end of every string in list
def remove_quotes(l):
    updated_list = []
    for i in l:
        updated_list.append(i[1:-1])
    return updated_list


def retrieve_data(u, h):
    try:
        r = requests.request("GET", u, headers=h)

        data1 = json.loads(r.text)  # data1 is a dictionary of all the data from the website

        data2 = json.dumps(data1)  # data2 is a string version of data1

        items = data2.split("usItemId")  # separates different products into strings and stores them in items

        items.pop(0)  # removes irrelevant information

        items_updated1 = []
        items_updated2 = []  # final list of products and data

        # loop that determines if the item is a product (every product has a fitment label)
        for element in items:
            if 'fitmentLabel' in element:
                items_updated1.append(element)

        # only adds products with a description to the list
        for element in items_updated1:
            if '"shortDescription": null' in element:
                continue
            else:
                if '<li>' in element:  # very few products have <li> in their description so those are excluded
                    continue
                else:
                    items_updated2.append(element)

        for i in items_updated2:
            item_split1 = []  # placeholder
            item_split2 = []  # holds names of product at index 0
            item_split3 = []  # holds brand name of product at index 0
            item_split4 = []  # placeholder
            item_split5 = []  # holds description of product at index 0
            item_split6 = []  # holds url of image of product at index 0
            item_split7 = []  # placeholder
            item_split8 = []  # holds price of product at index 0

            item_split1 = i.split(', "name": ')
            item_split2 = item_split1[1].split(
                ', "checkStoreAvailabilityATC": false, "seeShippingEligibility": false, "brand":')
            item_split2 = remove_quotes(item_split2)

            item_split3 = item_split2[1].split(', "type":')
            item_split3 = remove_quotes(item_split3)

            item_split4 = item_split3[1].split('"VARIANT", "shortDescription": ')
            item_split5 = item_split4[1].split(
                ', "weightIncrement": 1, "topResult": false, "imageInfo": {"thumbnailUrl":')
            item_split5 = remove_quotes(item_split5)

            # catches bug when description has html code and removes product
            if '<span' in item_split5[0]:
                continue

            item_split6 = item_split5[1].split(', "size"')
            item_split6 = remove_quotes(item_split6)

            item_split7 = i.split('"priceDisplay": ')
            item_split8 = item_split7[1].split('}, ')
            item_split8 = remove_quotes(item_split8)

            # when an item is on sale the price includes "Now", this statement removes the "Now" and keeps price at
            # the discount
            if 'Now ' in item_split8[0]:
                item_split8[0] = item_split8[0][4:]

            item_split8[0] = item_split8[0][1:]  # removes $

            # print("Name: " + item_split2[0] + " Brand: " + item_split3[0] + " Desc: " + item_split5[0] + " IMG: " +
            # item_split6[0] + " Price: " + item_split8[0])

            final_product = [item_split2[0], item_split3[0], item_split5[0], item_split6[0], item_split8[0]]

            products.append(final_product)

    except:
        print('Failed to add product')


def print_products_to_file():
    with open('products.txt', 'w') as f:
        for i in range(len(products)):
            # id = i + 1
            f.write(str(i + 1))
            for j in range(len(products[i])):
                f.write('|')
                f.write(products[i][j])
            f.write('|')
            f.write(str(random.randint(10, 35)))
            f.write('\n')


def main():
    retrieve_data(url_m, headers_m)
    retrieve_data(url_w, headers_w)
    retrieve_data(url_b, headers_b)
    retrieve_data(url_g, headers_g)

    print_products_to_file()


if __name__ == "__main__":
    main()