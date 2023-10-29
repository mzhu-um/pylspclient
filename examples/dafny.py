import pylspclient
import subprocess
import threading
import argparse


CAPABILITIES = {
    "workspace": {
        "applyEdit": True,
        "workspaceEdit": {
            "documentChanges": True,
            "resourceOperations": [
                "create",
                "rename",
                "delete"
            ],
            "failureHandling": "textOnlyTransactional",
            "normalizesLineEndings": True,
            "changeAnnotationSupport": {
                "groupsOnLabel": True
            }
        },
        "configuration": True,
        "didChangeWatchedFiles": {
            "dynamicRegistration": False,
            "relativePatternSupport": True
        },
        "symbol": {
            "dynamicRegistration": False,
            "symbolKind": {
                "valueSet": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26
                ]
            },
            "tagSupport": {
                "valueSet": [
                    1
                ]
            },
            "resolveSupport": {
                "properties": [
                    "location.range"
                ]
            }
        },
        "codeLens": {
            "refreshSupport": True
        },
        "executeCommand": {
            "dynamicRegistration": False
        },
        "didChangeConfiguration": {
            "dynamicRegistration": False
        },
        "workspaceFolders": True,
        "foldingRange": {
            "refreshSupport": True
        },
        "semanticTokens": {
            "refreshSupport": True
        },
        "fileOperations": {
            "dynamicRegistration": False,
            "didCreate": True,
            "didRename": True,
            "didDelete": True,
            "willCreate": True,
            "willRename": True,
            "willDelete": True
        },
        "inlineValue": {
            "refreshSupport": True
        },
        "inlayHint": {
            "refreshSupport": True
        },
        "diagnostics": {
            "refreshSupport": True
        }
    },
    "textDocument": {
        "publishDiagnostics": {
            "relatedInformation": True,
            "versionSupport": False,
            "tagSupport": {
                "valueSet": [
                    1,
                    2
                ]
            },
            "codeDescriptionSupport": True,
            "dataSupport": True
        },
        "synchronization": {
            "dynamicRegistration": False,
            "willSave": True,
            "willSaveWaitUntil": True,
            "didSave": True
        },
        "completion": {
            "dynamicRegistration": False,
            "contextSupport": True,
            "completionItem": {
                "snippetSupport": True,
                "commitCharactersSupport": True,
                "documentationFormat": [
                    "markdown",
                    "plaintext"
                ],
                "deprecatedSupport": True,
                "preselectSupport": True,
                "tagSupport": {
                    "valueSet": [
                        1
                    ]
                },
                "insertReplaceSupport": True,
                "resolveSupport": {
                    "properties": [
                        "documentation",
                        "detail",
                        "additionalTextEdits"
                    ]
                },
                "insertTextModeSupport": {
                    "valueSet": [
                        1,
                        2
                    ]
                },
                "labelDetailsSupport": True
            },
            "insertTextMode": 2,
            "completionItemKind": {
                "valueSet": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25
                ]
            },
            "completionList": {
                "itemDefaults": [
                    "commitCharacters",
                    "editRange",
                    "insertTextFormat",
                    "insertTextMode",
                    "data"
                ]
            }
        },
        "hover": {
            "dynamicRegistration": False,
            "contentFormat": [
                "markdown",
                "plaintext"
            ]
        },
        "signatureHelp": {
            "dynamicRegistration": False,
            "signatureInformation": {
                "documentationFormat": [
                    "markdown",
                    "plaintext"
                ],
                "parameterInformation": {
                    "labelOffsetSupport": True
                },
                "activeParameterSupport": True
            },
            "contextSupport": True
        },
        "definition": {
            "dynamicRegistration": False,
            "linkSupport": True
        },
        "references": {
            "dynamicRegistration": False
        },
        "documentHighlight": {
            "dynamicRegistration": False
        },
        "documentSymbol": {
            "dynamicRegistration": False,
            "symbolKind": {
                "valueSet": [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    13,
                    14,
                    15,
                    16,
                    17,
                    18,
                    19,
                    20,
                    21,
                    22,
                    23,
                    24,
                    25,
                    26
                ]
            },
            "hierarchicalDocumentSymbolSupport": True,
            "tagSupport": {
                "valueSet": [
                    1
                ]
            },
            "labelSupport": True
        },
        "codeAction": {},
        "codeLens": {
            "dynamicRegistration": False
        },
        "formatting": {
            "dynamicRegistration": False
        },
        "rangeFormatting": {
            "dynamicRegistration": False,
            "rangesSupport": True
        },
        "onTypeFormatting": {
            "dynamicRegistration": False
        },
        "rename": {},
        "documentLink": {
            "dynamicRegistration": False,
            "tooltipSupport": True
        },
        "typeDefinition": {
            "dynamicRegistration": False,
            "linkSupport": True
        },
        "implementation": {
            "dynamicRegistration": False,
            "linkSupport": True
        },
        "colorProvider": {
            "dynamicRegistration": False
        },
        "foldingRange": {
            "dynamicRegistration": False,
            "rangeLimit": 5000,
            "lineFoldingOnly": True,
            "foldingRangeKind": {
                "valueSet": [
                    "comment",
                    "imports",
                    "region"
                ]
            },
            "foldingRange": {
                "collapsedText": False
            }
        },
        "declaration": {
            "dynamicRegistration": False,
            "linkSupport": True
        },
        "selectionRange": {
            "dynamicRegistration": False
        },
        "callHierarchy": {
            "dynamicRegistration": False
        },
        "semanticTokens": {
            "dynamicRegistration": False,
            "tokenTypes": [
                "namespace",
                "type",
                "class",
                "enum",
                "interface",
                "struct",
                "typeParameter",
                "parameter",
                "variable",
                "property",
                "enumMember",
                "event",
                "function",
                "method",
                "macro",
                "keyword",
                "modifier",
                "comment",
                "string",
                "number",
                "regexp",
                "operator",
                "decorator"
            ],
            "tokenModifiers": [
                "declaration",
                "definition",
                "readonly",
                "static",
                "deprecated",
                "abstract",
                "async",
                "modification",
                "documentation",
                "defaultLibrary"
            ],
            "formats": [
                "relative"
            ],
            "requests": {
                "range": True,
                "full": {
                    "delta": True
                }
            },
            "multilineTokenSupport": False,
            "overlappingTokenSupport": False,
            "serverCancelSupport": True,
            "augmentsSyntaxTokens": True
        },
        "linkedEditingRange": {
            "dynamicRegistration": False
        },
        "typeHierarchy": {
            "dynamicRegistration": False
        },
        "inlineValue": {
            "dynamicRegistration": False
        },
        "inlayHint": {
            "dynamicRegistration": False,
            "resolveSupport": {
                "properties": [
                    "tooltip",
                    "textEdits",
                    "label.tooltip",
                    "label.location",
                    "label.command"
                ]
            }
        },
        "diagnostic": {
            "dynamicRegistration": False,
            "relatedDocumentSupport": False
        }
    },
    "window": {
        "showMessage": {
            "messageActionItem": {
                "additionalPropertiesSupport": True
            }
        },
        "showDocument": {
            "support": True
        },
        "workDoneProgress": True
    },
    "general": {
        "staleRequestSupport": {
            "cancel": True,
            "retryOnContentModified": [
                "textDocument/semanticTokens/full",
                "textDocument/semanticTokens/range",
                "textDocument/semanticTokens/full/delta"
            ]
        },
        "regularExpressions": {
            "engine": "ECMAScript",
            "version": "ES2020"
        },
        "markdown": {
            "parser": "marked",
            "version": "1.1.0"
        },
        "positionEncodings": [
            "utf-16"
        ]
    },
    "notebookDocument": {
        "synchronization": {
            "dynamicRegistration": False,
            "executionSummarySupport": True
        }
    }
}

class ReadPipe(threading.Thread):
    def __init__(self, pipe):
        threading.Thread.__init__(self)
        self.pipe = pipe

    def run(self):
        line = self.pipe.readline().decode('utf-8')
        while line:
            print(line)
            line = self.pipe.readline().decode('utf-8')

def blame(response):
    for d in response['diagnostics']:
        if d['severity'] == 1:
            print(f"An error occurs in {response['uri']} at {d['range']}:")
            print(f"\t[{d['source']}] {d['message']}")

            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dafny @ pylspclient')
    parser.add_argument('dafny_path', type=str, default="/home/mzhu/github/dafny/Scripts/dafny", 
                    help='the dafny path', nargs="?")
    args = parser.parse_args()
    p = subprocess.Popen([args.dafny_path,
                          "server",
                          "--verify-on:Change",
                          "--verification-time-limit:4",
                          "--cache-verification=0",
                          "--cores:9",
                          "--notify-ghostness:false",
                          "--notify-line-verification-status:false",
                          # "--log-format:text"
                          ],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    read_pipe = ReadPipe(p.stderr)
    read_pipe.start()
    json_rpc_endpoint = pylspclient.JsonRpcEndpoint(p.stdin, p.stdout)
    # To work with socket: sock_fd = sock.makefile()
    callbacks = {
        "dafny/compilation/status" : print,
        # "dafny/verification/status/gutter" : print,
        "dafny/textDocument/symbolStatus": print,
        "textDocument/publishDiagnostics": blame,
    }
    lsp_endpoint = pylspclient.LspEndpoint(json_rpc_endpoint,
                                           notify_callbacks=callbacks)
    lsp_client = pylspclient.LspClient(lsp_endpoint)
    capabilities = CAPABILITIES

    root_uri = "file:///home/mzhu/tmp/p2"
    workspace_folders = [{'name': 'p2', 'uri': root_uri}]
    print(lsp_client.initialize(p.pid, None, root_uri, None, capabilities, "off", workspace_folders))
    print(lsp_client.initialized())

    file_name = "merge.dfy"
    uri = root_uri + "/" + file_name
    text = open("/home/mzhu/tmp/p2/merge.dfy", "r").read()
    languageId = "dafny"
    version = 1
    lsp_client.didOpen(
        pylspclient.lsp_structs.TextDocumentItem(
            uri, languageId, version, text))

    try:
        symbols = lsp_client.documentSymbol(pylspclient.lsp_structs.TextDocumentIdentifier(uri))
        for symbol in symbols:
            print(symbol.name)
    except pylspclient.lsp_structs.ResponseError:
        # documentSymbol is supported from version 8.
        print("Failed to document symbols")

    # lsp_client.shutdown()
    # lsp_client.exit()
