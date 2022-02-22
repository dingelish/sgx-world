with open("deps.txt") as f:
    lines = f.readlines()

#print(len(lines))

crates = {}

for line in lines:
    splitted = line.strip().split(' ')
    crate_name = splitted[0]
    crate_dir = splitted[1]
    if crate_dir in crates:
        crates[crate_dir].append(crate_name)
    else:
        crates[crate_dir] = [crate_name]

#print(crates)
patches = {}

special_crates = {"webpki", "webpki-roots", "sct", "rustls"}

sub_folder_crates = {
        "serde":"serde",
        "serde_derive":"serde_derive",
        "serde_derive_internals":"serde_derive_internals",
        "serde_test":"serde_test",
        "blobby":"blobby",
        "byte-tools":"byte-tools",
        "block-buffer":"block-buffer",
        "block-padding":"block-padding",
        "hex-literal-impl":"hex-literal/hex-literal-impl",
        "hex-literal":"hex-literal",
        "prost-types":"prost-types",
        "percent-encoding":"percent_encoding",
        "idna":"idna",
        "data-url":"data-url",
        "etcommon-rlp":"rlp",
        "etcommon-bigint":"bigint",
        "etcommon-hexutil":"hexutil",
        "etcommon-block":"block",
        "etcommon-block-core":"block-core",
        "etcommon-trie":"trie",
        "etcommon-bloom":"bloom",
        "whirlpool":"whirlpool",
        "ripemd160":"ripemd160",
        "blake2":"blake2",
        "md2":"md2",
        "gost94":"gost94",
        "md-5":"md5",
        "groestl":"groestl",
        "sha2":"sha2",
        "md4":"md4",
        "sha-1":"sha1",
        "streebog":"streebog",
        "sha3":"sha3",
        "ripemd320":"ripemd320",
        "aes":"aes/aes",
        "aes-soft":"aes/aes-soft",
        "aesni":"aes/aesni",
        "block-modes":"block-modes",
        "blowfish":"blowfish",
        "cast5":"cast5",
        "des":"des",
        "kuznyechik":"kuznyechik",
        "magma":"magma",
        "rc2":"rc2",
        "twofish":"twofish",
        "cmac":"cmac",
        "daa":"daa",
        "hmac":"hmac",
        "aes-ctr":"aes-ctr",
        "cfb8":"cfb8",
        "cfb-mode":"cfb-mode",
        "chacha20":"chacha20",
        "ctr":"ctr",
        "ofb":"ofb",
        "salsa20":"salsa20",
        "salsa20-core":"salsa20-core",
        "aead":"aead",
        "block-cipher-trait":"block-cipher-trait",
        "crypto-mac":"crypto-mac",
        "digest":"digest",
        "stream-cipher":"stream-cipher",
        "universal-hash":"universal-hash",
        "protobuf":"protobuf",
        "parity-bytes":"parity-bytes",
        "kvdb":"kvdb",
        "kvdb-memorydb":"kvdb-memorydb",
        "blake-hash":"hashes/blake",
        "groestl-aesni":"hashes/groestl",
        "jh-x86_64":"hashes/jh",
        "skein-hash":"hashes/skein",
        "c2-chacha":"stream-ciphers/chacha",
        "ppv-lite86":"utils-simd/ppv-lite86",
        "threefish-cipher":"block-ciphers/threefish",
        "typetag-impl":"impl",
        "wasmi-validation":"validation",
        "inventory-impl":"impl",
        "failure_derive":"failure_derive",
        "regex-syntax":"regex-syntax",
        "ucd-util":"ucd-util",
        "rustls":"rustls",
        "thiserror-impl":"impl",
        "matches":"matches",
        "parity-scale-codec-derive":"derive",
        "miniz_oxide": "miniz_oxide",
        "futures": "futures",
        "futures-channel": "futures-channel",
        "futures-core": "futures-core",
        "futures-executor": "futures-executor",
        "futures-io": "futures-io",
        "futures-macro": "futures-macro",
        "futures-sink": "futures-sink",
        "futures-task": "futures-task",
        "futures-util": "futures-util",
        "rand_core":"rand_core",
        "rand_chacha":"rand_chacha",
        "rmp":"rmp",
        "rmp-serde":"rmp-serde",
        "rmpv":"rmpv",
        }

for k, v in crates.items():
    repo_name = 'https://github.com/mesalock-linux/' + k
    patches[repo_name] = []
    v = list(set(v))
    for crate_name in v:
        patch_path = k 
        if crate_name == "num-bigint-dig":
            patch_path = "num-bigint-dig-sgx"

        if crate_name in special_crates:
            patch_path = patch_path + "-sgx"

        if crate_name in sub_folder_crates:
            patch_path = patch_path + "/" +sub_folder_crates[crate_name] 
        patch_line = '{} = {{ path = "../{}" }}'.format(crate_name, patch_path)
        patches[repo_name].append(patch_line)
        #print(patch_line)

lines = []

for k, v in patches.items():
    lines.append('[patch."{}"]\n'.format(k))
    for l in v:
        lines.append(l)
        lines.append('\n')
    lines.append('\n')

with open("deps_patch.txt", "w") as f:
    f.writelines(lines)
