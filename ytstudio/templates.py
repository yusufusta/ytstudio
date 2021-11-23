class Templates:
    channelId = ""
    videoId = ""
    sessionToken = ""
    botguardResponse = ""
    delegatedSessionId = ""

    CLIENT = {
        "clientName": 62,
        "clientVersion": "1.20201130.03.00",
        "hl": "en-GB",
        "gl": "PL",
        "experimentsToken": "",
        "utcOffsetMinutes": 60
    }

    def __init__(self, config) -> None:
        self.config = config
        self.channelId = self.config["channelId"]
        self.sessionToken = self.config["sessionToken"]
        self.botguardResponse = self.config["botguardResponse"] if "botguardResponse" in self.config else ""
        self.delegatedSessionId = self.config["delegatedSessionId"] if "delegatedSessionId" in self.config else ""
        self._()

    def setVideoId(self, videoId):
        self.videoId = videoId
        self._()

    def _(self):
        self.DELETE_VIDEO = {
            "videoId": self.videoId,
            "context": {
                "client": self.CLIENT,
                "request": {
                    "returnLogEntry": True,
                    "internalExperimentFlags": [],
                    "sessionInfo": {
                        "token": self.sessionToken
                    }
                },
                "user": {
                    "delegationContext": {
                        "roleType": {
                            "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                        },
                        "externalChannelId": self.channelId
                    },
                    "serializedDelegationContext": ""
                },
                "clientScreenNonce": ""
            },
            "delegationContext": {
                "roleType": {
                    "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                },
                "externalChannelId": self.channelId
            }
        }

        self.UPLOAD_VIDEO = {
            "channelId": self.channelId,
            "resourceId": {
                "scottyResourceId": {
                    "id": ""
                }
            },
            "frontendUploadId": "",
            "initialMetadata": {
                "title": {
                    "newTitle": ""
                },
                "description": {
                    "newDescription": "",
                    "shouldSegment": True
                },
                "privacy": {
                    "newPrivacy": ""
                },
                "draftState": {
                    "isDraft": ""
                }
            },
            "context": {
                "client": self.CLIENT,
                "request": {
                    "returnLogEntry": True,
                    "internalExperimentFlags": [],
                    "sessionInfo": {
                        "token": self.sessionToken
                    }
                },
                "user": {
                    "onBehalfOfUser": self.delegatedSessionId,
                    "delegationContext": {
                        "externalChannelId": self.channelId,
                        "roleType": {
                            "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                        }
                    },
                    "serializedDelegationContext": ""
                },
                "clientScreenNonce": ""
            },
            "delegationContext": {
                "roleType": {
                    "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                },
                "externalChannelId": self.channelId
            }
        }

        if self.botguardResponse and self.botguardResponse != "":
            self.UPLOAD_VIDEO["botguardClientResponse"] = self.botguardResponse

        self.METADATA_UPDATE = {
            "encryptedVideoId": self.videoId,
            "videoReadMask": {
                "channelId": True,
                "videoId": True,
                "lengthSeconds": True,
                "premiere": {
                    "all": True
                },
                "status": True,
                "thumbnailDetails": {
                    "all": True
                },
                "title": True,
                "draftStatus": True,
                "downloadUrl": True,
                "watchUrl": True,
                "permissions": {
                    "all": True
                },
                "timeCreatedSeconds": True,
                "timePublishedSeconds": True,
                "origin": True,
                "livestream": {
                    "all": True
                },
                "privacy": True,
                "contentOwnershipModelSettings": {
                    "all": True
                },
                "features": {
                    "all": True
                },
                "responseStatus": {
                    "all": True
                },
                "statusDetails": {
                    "all": True
                },
                "description": True,
                "metrics": {
                    "all": True
                },
                "publicLivestream": {
                    "all": True
                },
                "publicPremiere": {
                    "all": True
                },
                "titleFormattedString": {
                    "all": True
                },
                "descriptionFormattedString": {
                    "all": True
                },
                "audienceRestriction": {
                    "all": True
                },
                "monetization": {
                    "all": True
                },
                "selfCertification": {
                    "all": True
                },
                "allRestrictions": {
                    "all": True
                },
                "inlineEditProcessingStatus": True,
                "videoPrechecks": {
                    "all": True
                },
                "videoResolutions": {
                    "all": True
                },
                "scheduledPublishingDetails": {
                    "all": True
                },
                "visibility": {
                    "all": True
                },
                "privateShare": {
                    "all": True
                },
                "sponsorsOnly": {
                    "all": True
                },
                "unlistedExpired": True,
                "videoTrailers": {
                    "all": True
                }
            },
            "context": {
                "client": self.CLIENT,
                "request": {
                    "returnLogEntry": True,
                    "internalExperimentFlags": [],
                    "sessionInfo": {
                        "token": self.sessionToken
                    }
                },
                "user": {
                    "delegationContext": {
                        "externalChannelId": self.channelId,
                        "roleType": {
                            "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                        }
                    },
                    "serializedDelegationContext": ""
                },
                "clientScreenNonce": ""
            },
            "delegationContext": {
                "externalChannelId": self.channelId,
                "roleType": {
                    "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                }
            }
        }

        self.METADATA_UPDATE_MONETIZATION = {
            "monetizationSettings": {
                "newMonetizeWithAds": True
            }
        }

        self.LIST_VIDEOS = {
            "filter": {
                "and": {
                    "operands": [
                        {
                            "channelIdIs": {
                                "value": self.channelId
                            }
                        }, {
                            "videoOriginIs": {
                                "value": "VIDEO_ORIGIN_UPLOAD"
                            }
                        }
                    ]
                }
            },
            "order": "VIDEO_ORDER_DISPLAY_TIME_DESC",
            "pageSize": 30,
            "mask": {
                "channelId": True,
                "videoId": True,
                "lengthSeconds": True,
                "premiere": {
                    "all": True
                },
                "status": True,
                "thumbnailDetails": {
                    "all": True
                },
                "title": True,
                "draftStatus": True,
                "downloadUrl": True,
                "watchUrl": True,
                "permissions": {
                    "all": True
                },
                "timeCreatedSeconds": True,
                "timePublishedSeconds": True,
                "origin": True,
                "livestream": {
                    "all": True
                },
                "privacy": True,
                "contentOwnershipModelSettings": {
                    "all": True
                },
                "features": {
                    "all": True
                },
                "responseStatus": {
                    "all": True
                },
                "statusDetails": {
                    "all": True
                },
                "description": True,
                "metrics": {
                    "all": True
                },
                "publicLivestream": {
                    "all": True
                },
                "publicPremiere": {
                    "all": True
                },
                "titleFormattedString": {
                    "all": True
                },
                "descriptionFormattedString": {
                    "all": True
                },
                "audienceRestriction": {
                    "all": True
                },
                "monetization": {
                    "all": True
                },
                "selfCertification": {
                    "all": True
                },
                "allRestrictions": {
                    "all": True
                },
                "inlineEditProcessingStatus": True,
                "videoPrechecks": {
                    "all": True
                },
                "videoResolutions": {
                    "all": True
                },
                "scheduledPublishingDetails": {
                    "all": True
                },
                "visibility": {
                    "all": True
                },
                "privateShare": {
                    "all": True
                },
                "sponsorsOnly": {
                    "all": True
                },
                "unlistedExpired": True,
                "videoTrailers": {
                    "all": True
                }
            },
            "context": {
                "client": self.CLIENT,
                "request": {
                    "returnLogEntry": True,
                    "internalExperimentFlags": []
                },
                "user": {
                    "delegationContext": {
                        "externalChannelId": self.channelId,
                        "roleType": {
                            "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                        }
                    },
                    "serializedDelegationContext": ""
                },
                "clientScreenNonce": ""
            }
        }

        self.GET_VIDEO = {
            "context": {
                "client": self.CLIENT,
                "request": {
                    "returnLogEntry": True,
                    "internalExperimentFlags": []
                },
                "user": {
                    "delegationContext": {
                        "externalChannelId": self.channelId,
                        "roleType": {
                            "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                        }
                    },
                    "serializedDelegationContext": ""
                },
                "clientScreenNonce": ""
            },
            "failOnError": True,
            "videoIds": [self.videoId],
            "mask": {
                "downloadUrl": True,
                "origin": True,
                "premiere": {
                    "all": True
                },
                "privacy": True,
                "videoId": True,
                "status": True,
                "permissions": {
                    "all": True
                },
                "draftStatus": True,
                "statusDetails": {
                    "all": True
                },
                "inlineEditProcessingStatus": True,
                "selfCertification": {
                    "all": True
                },
                "monetization": {
                    "all": True
                },
                "allRestrictions": {
                    "all": True
                },
                "videoPrechecks": {
                    "all": True
                },
                "audienceRestriction": {
                    "all": True
                },
                "responseStatus": {
                    "all": True
                },
                "features": {
                    "all": True
                },
                "videoAdvertiserSpecificAgeGates": {
                    "all": True
                },
                "claimDetails": {
                    "all": True
                },
                "commentsDisabledInternally": True,
                "livestream": {
                    "all": True
                },
                "music": {
                    "all": True
                },
                "ownedClaimDetails": {
                    "all": True
                },
                "timePublishedSeconds": True,
                "uncaptionedReason": True,
                "remix": {
                    "all": True
                },
                "contentOwnershipModelSettings": {
                    "all": True
                },
                "channelId": True,
                "mfkSettings": {
                    "all": True
                },
                "thumbnailEditorState": {
                    "all": True
                },
                "thumbnailDetails": {
                    "all": True
                },
                "scheduledPublishingDetails": {
                    "all": True
                },
                "visibility": {
                    "all": True
                },
                "privateShare": {
                    "all": True
                },
                "sponsorsOnly": {
                    "all": True
                },
                "unlistedExpired": True,
                "videoTrailers": {
                    "all": True
                },
                "allowComments": True,
                "allowEmbed": True,
                "allowRatings": True,
                "ageRestriction": True,
                "audioLanguage": {
                    "all": True
                },
                "category": True,
                "commentFilter": True,
                "crowdsourcingEnabled": True,
                "dateRecorded": {
                    "all": True
                },
                "defaultCommentSortOrder": True,
                "description": True,
                "descriptionFormattedString": {
                    "all": True
                },
                "gameTitle": {
                    "all": True
                },
                "license": True,
                "liveChat": {
                    "all": True
                },
                "location": {
                    "all": True
                },
                "metadataLanguage": {
                    "all": True
                },
                "paidProductPlacement": True,
                "publishing": {
                    "all": True
                },
                "tags": {
                    "all": True
                },
                "title": True,
                "titleFormattedString": {
                    "all": True
                },
                "viewCountIsHidden": True,
                "autoChapterSettings": {
                    "all": True
                },
                "videoStreamUrl": True,
                "videoDurationMs": True,
                "videoEditorProject": {
                    "videoDimensions": {
                        "all": True
                    }
                },
                "originalFilename": True,
                "videoResolutions": {
                    "all": True
                }
            },
            "criticalRead": False
        }

        self.CREATE_PLAYLIST = {
            "title": "",
            "privacyStatus": "",
            "context": {
                "client": self.CLIENT,
                "request": {
                    "returnLogEntry": True,
                    "internalExperimentFlags": [],
                    "sessionInfo": {
                        "token": self.sessionToken
                    }
                },
                "user": {
                    "delegationContext": {
                        "externalChannelId": self.channelId,
                        "roleType": {
                            "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                        }
                    },
                    "serializedDelegationContext": ""
                },
                "clientScreenNonce": ""
            },
            "delegationContext": {
                "externalChannelId": self.channelId,
                "roleType": {
                    "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                }
            }
        }

        self.METADATA_UPDATE_PLAYLIST = {
            "addToPlaylist": {
                "addToPlaylistIds": [],
                "deleteFromPlaylistIds": []
            }
        }

        self.METADATA_UPDATE_TITLE = {
            "title": {
                "newTitle": "",
                "shouldSegment": True
            }
        }

        self.METADATA_UPDATE_DESCRIPTION = {
            "description": {
                "newDescription": "",
                "shouldSegment": True
            }
        }

        self.METADATA_UPDATE_TAGS = {
            "tags": {
                "newTags": [],
                "shouldSegment": True
            }
        }

        self.METADATA_UPDATE_CATEGORY = {
            "category": {
                "newCategoryId": 0
            }
        }

        self.METADATA_UPDATE_COMMENTS = {
            "commentOptions": {
                "newAllowComments": True,
                "newAllowCommentsMode": "ALL_COMMENTS",
                "newCanViewRatings": True,
                "newDefaultSortOrder": "MDE_COMMENT_SORT_ORDER_TOP"
            }
        }

        self.METADATA_UPDATE_PRIVACY = {
            "privacyState": {"newPrivacy": "PUBLIC"}
        }

        self.METADATA_UPDATE_THUMB = {
            "videoStill": {"operation": "UPLOAD_CUSTOM_THUMBNAIL", "image": {
                "dataUri": ""
            }}
        }
