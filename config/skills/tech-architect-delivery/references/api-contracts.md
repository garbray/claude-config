# API Design & Contract Specifications Guide

APIs are contracts between frontend and backend. Good API design prevents misunderstandings, enables parallel work, and makes integration smooth.

## REST API Design Principles

### Resource-Oriented Design

Think in terms of resources, not actions.

**Good** (resource-oriented):
```
GET    /api/articles              - List articles
POST   /api/articles              - Create article
GET    /api/articles/{id}         - Get specific article
PUT    /api/articles/{id}         - Update article
DELETE /api/articles/{id}         - Delete article

GET    /api/articles/{id}/comments         - Get article's comments
POST   /api/articles/{id}/comments         - Add comment to article
DELETE /api/articles/{id}/comments/{cid}   - Delete comment
```

**Bad** (action-oriented):
```
POST /api/createArticle
POST /api/updateArticle
POST /api/deleteArticle
POST /api/getArticleComments
POST /api/addCommentToArticle
```

### HTTP Methods & Status Codes

Use HTTP methods correctly:

```
GET:    Retrieve resource, safe, idempotent
POST:   Create resource or perform action
PUT:    Replace entire resource, idempotent
PATCH:  Partial update, idempotent
DELETE: Delete resource, idempotent

Status Codes:
200 OK              - Request succeeded
201 Created         - Resource created
204 No Content      - Success, no body
400 Bad Request     - Invalid request (client error)
401 Unauthorized    - Auth required or invalid
403 Forbidden       - Auth ok, but access denied
404 Not Found       - Resource doesn't exist
409 Conflict        - Conflict (e.g., duplicate)
429 Too Many Requests - Rate limit exceeded
500 Internal Server Error - Server error
503 Service Unavailable - Temporary outage
```

### Request Payloads

**Provide Clear Examples**:
```
POST /api/articles
Content-Type: application/json

Request:
{
  "title": "Getting Started with APIs",
  "body": "This article explains REST APIs...",
  "tags": ["api", "rest", "tutorial"],
  "published": false
}

Response: 201 Created
{
  "id": "article-123",
  "title": "Getting Started with APIs",
  "body": "This article explains REST APIs...",
  "tags": ["api", "rest", "tutorial"],
  "published": false,
  "authorId": "user-456",
  "createdAt": "2024-12-20T10:00:00Z",
  "updatedAt": "2024-12-20T10:00:00Z"
}
```

**Document Constraints**:
```
Fields:
- title (string, required, 1-200 characters)
- body (string, required, 1-50000 characters)
- tags (array of strings, optional, max 10 tags, each 1-50 characters)
- published (boolean, optional, default false)

Validation:
- title cannot be empty
- body cannot be empty
- tags cannot contain duplicates
- Each tag must be alphanumeric + hyphens only
```

### Response Payloads

**Consistent Structure**:
```
Success Response:
{
  "data": { /* actual data */ },
  "meta": { /* optional metadata */ }
}

Error Response:
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Article not found",
    "details": [ /* optional */ ]
  }
}

List Response (with Pagination):
{
  "data": [ /* array of items */ ],
  "pagination": {
    "offset": 0,
    "limit": 20,
    "total": 150,
    "hasMore": true
  }
}
```

**Keep It Consistent**:
- All success responses use `{ data, meta }`
- All error responses use `{ error: { code, message, details } }`
- Paginated responses always have `pagination` object
- Timestamps always in ISO 8601 format

### Pagination

```
Query Parameters:
- limit: integer, 1-100, default 20
- offset: integer, >= 0, default 0

Response:
{
  "data": [ /* items */ ],
  "pagination": {
    "offset": 0,
    "limit": 20,
    "total": 150,
    "hasMore": true
  }
}

Cursor-Based (for mobile/infinite scroll):
Query Parameters:
- limit: integer, 1-100, default 20
- cursor: string, optional

Response:
{
  "data": [ /* items */ ],
  "pagination": {
    "cursor": "abc123xyz",
    "hasMore": true
  }
}
```

### Filtering & Sorting

```
GET /api/articles?status=published&sort=-createdAt

Filters:
- status: 'draft' | 'published' | 'archived'
- author: user ID
- tag: tag name
- dateFrom: ISO 8601 date
- dateTo: ISO 8601 date

Sorting:
- sort: field name
- Prefix with - for descending (e.g., -createdAt)
- Default sort specified in API docs

Implementation Notes:
- Validate filter values
- Prevent injections (validate against allowed fields)
- Index filtered columns for performance
- Document performance implications of filters
```

## Error Handling

### Error Response Format

```
Standard Error Response:
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "One or more fields are invalid",
    "details": [
      {
        "field": "email",
        "message": "Must be valid email address",
        "value": "invalid-email"
      },
      {
        "field": "password",
        "message": "Must be at least 8 characters",
        "value": null
      }
    ]
  }
}

Error Codes (Define Exhaustively):
CLIENT_ERRORS:
- INVALID_REQUEST        - Malformed request
- VALIDATION_ERROR       - Field validation failed
- RESOURCE_NOT_FOUND     - Resource doesn't exist
- RESOURCE_CONFLICT      - Conflict (duplicate, etc.)
- RATE_LIMIT_EXCEEDED    - Too many requests

AUTH_ERRORS:
- AUTH_REQUIRED          - No auth token provided
- AUTH_INVALID           - Invalid/expired token
- FORBIDDEN              - Insufficient permissions
- SESSION_EXPIRED        - Session timed out

SERVER_ERRORS:
- INTERNAL_ERROR         - Server error
- SERVICE_UNAVAILABLE    - Temporary outage
- DEPENDENCY_FAILED      - External service failed
```

### HTTP Status Code Strategy

```
1xx (Informational)     - Rarely used in APIs
2xx (Success)           - Request succeeded
  200 OK                - General success
  201 Created           - Resource created
  204 No Content        - Success, no body
  
3xx (Redirection)       - Rarely used in modern APIs
  301/302               - Moved/redirect
  
4xx (Client Error)      - Client's fault
  400 Bad Request       - Malformed request
  401 Unauthorized      - Auth required/invalid
  403 Forbidden         - Insufficient permissions
  404 Not Found         - Resource missing
  409 Conflict          - Duplicate/conflict
  429 Too Many Requests - Rate limited
  
5xx (Server Error)      - Server's fault
  500 Internal Error    - Unhandled server error
  503 Unavailable       - Temporary outage
```

## Authentication & Authorization

### Token-Based Auth (JWT)

```
Request:
POST /api/auth/login
{
  "email": "user@example.com",
  "password": "password123"
}

Response: 200 OK
{
  "accessToken": "eyJhbGc...",
  "refreshToken": "eyJhbGc...",
  "expiresIn": 3600
}

Usage (all requests):
GET /api/articles
Authorization: Bearer eyJhbGc...

Token Contents:
{
  "sub": "user-123",           // Subject (user ID)
  "iat": 1640000000,           // Issued at
  "exp": 1640003600,           // Expiration (1 hour)
  "scope": "articles:read articles:write"
}

Refresh:
POST /api/auth/refresh
{
  "refreshToken": "eyJhbGc..."
}

Response: 200 OK
{
  "accessToken": "eyJhbGc...",
  "expiresIn": 3600
}
```

### Permission Scopes

```
Scope Format: resource:action

Examples:
- articles:read       - Can read articles
- articles:write      - Can create/update articles
- articles:delete     - Can delete articles
- profile:read        - Can read own profile
- profile:write       - Can update own profile
- admin:read          - Admin read access
- admin:write         - Admin write access

Usage in API:
GET /api/articles               - Requires articles:read
POST /api/articles              - Requires articles:write
DELETE /api/articles/{id}       - Requires articles:delete
PUT /api/profile                - Requires profile:write
GET /api/admin/users            - Requires admin:read

Server-Side Enforcement:
1. Validate token is valid
2. Check expiration
3. Verify scope is present
4. Verify resource ownership (if needed)
```

## Real-Time Communication

### WebSocket Protocol

```
Connection Lifecycle:

CONNECT (Client → Server):
{
  "type": "CONNECT",
  "userId": "user-123"
}

Server Response:
{
  "type": "CONNECTED",
  "connectionId": "conn-abc123"
}

SUBSCRIBE (Client → Server):
{
  "type": "SUBSCRIBE",
  "channel": "articles:{articleId}:comments"
}

Server Response:
{
  "type": "SUBSCRIBED",
  "channel": "articles:123:comments"
}

MESSAGE (Server → Client):
{
  "type": "MESSAGE",
  "channel": "articles:123:comments",
  "data": {
    "id": "comment-456",
    "text": "Great article!",
    "authorId": "user-789",
    "createdAt": "2024-12-20T10:30:00Z"
  }
}

DISCONNECT (Client → Server):
{
  "type": "DISCONNECT"
}

Reconnection:
- Automatic with exponential backoff
- Subscribe to previous channels after reconnect
- Catch up on missed messages via HTTP API
```

### Server-Sent Events (SSE)

```
GET /api/stream/user/{userId}
Accept: text/event-stream

Response:
event: message
data: {"type":"favorite","itemId":"123"}

event: notification
data: {"type":"comment","articleId":"456"}

event: keepalive
data: {}

Client:
const eventSource = new EventSource('/api/stream/user/123');
eventSource.onmessage = (e) => {
  const data = JSON.parse(e.data);
  // Handle message
};
```

## Data Model Contracts

### Entity Definitions

```
Entity: User

Fields:
- id (UUID, PK)
  Description: Unique identifier
  Immutable: yes
  
- email (string, unique)
  Description: Email address
  Format: RFC 5322 email
  Immutable: no (can change but creates new session)
  
- passwordHash (string)
  Description: Hashed password
  Immutable: no
  Sensitive: yes (never exposed in API)
  
- firstName (string, optional)
  Length: 1-100 characters
  
- lastName (string, optional)
  Length: 1-100 characters
  
- createdAt (ISO 8601 timestamp)
  Description: When user created account
  Immutable: yes
  
- updatedAt (ISO 8601 timestamp)
  Description: Last profile update
  Immutable: no

Relationships:
- Has many Articles (one user, many articles)
- Has many Comments (one user, many comments)

Constraints:
- email must be unique
- firstName + lastName together form display name
- email cannot be changed to another user's email

Lifecycle:
- CREATED: User registers
- ACTIVE: Normal state
- DEACTIVATED: User requested deactivation (soft delete)
- DELETED: Hard delete (rare, legal compliance)

API Representations:

Public Profile (anyone can see):
{
  "id": "user-123",
  "firstName": "Jane",
  "lastName": "Smith",
  "createdAt": "2024-01-15T00:00:00Z"
}

Private Profile (user sees own):
{
  "id": "user-123",
  "email": "jane@example.com",
  "firstName": "Jane",
  "lastName": "Smith",
  "createdAt": "2024-01-15T00:00:00Z",
  "updatedAt": "2024-12-20T10:00:00Z"
}

Note: passwordHash never exposed in API
```

## API Versioning

```
Option 1: URL Path Versioning
GET /api/v1/articles
GET /api/v2/articles

Option 2: Header Versioning
GET /api/articles
Accept: application/vnd.api+json;version=2

Preferred: URL Path (clearer, easier to debug)

Version Strategy:
- v1: Initial release
- v2: Major breaking change (add new endpoints, deprecate old)
- Maintain backward compat for 6 months
- Send deprecation warnings in response headers

Deprecation Header:
Deprecation: true
Sunset: Sun, 20 Jun 2025 23:59:59 GMT
Link: </api/v2/articles>; rel="successor-version"
```

## Rate Limiting

```
Request:
GET /api/articles

Response Headers:
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640020000

When Exceeded:
HTTP 429 Too Many Requests

{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests",
    "retryAfter": 60
  }
}

Strategies:
- Per-user rate limiting (100 requests/hour)
- IP-based fallback (1000 requests/hour)
- Burst allowance (allow 10 requests/second, 100/minute)
- Different limits for different endpoints

Best Practice:
- Document limits clearly
- Provide remaining count
- Help users understand when they're approaching limit
- Graceful degradation instead of hard blocks
```

## API Documentation

When documenting APIs, include:

```
Endpoint: [METHOD] /path

Description:
What this endpoint does

Authentication:
Required: yes/no
Scope: articles:read

Request:
- Parameters (query, path, body)
- Example request
- Constraints and validation

Response:
- Success (200/201/204): Example response
- Error cases (400/401/403/404/429/500): Example error

Example:

---
GET /api/articles/{id}

Get a specific article by ID

Authentication: Required
Scope: articles:read

Parameters:
- id (path, string, required): Article ID

Response:
200 OK
{
  "data": {
    "id": "article-123",
    "title": "...",
    ...
  }
}

404 Not Found
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "Article not found"
  }
}
```

## Contract Testing

Ensure frontend and backend implement the contract:

```
Test: API Returns Expected Response

Given: User has auth token
When: GET /api/users/{id}
Then: Response has status 200
And: Response body includes id, email, createdAt
And: Response time < 500ms

Test: API Validates Input

Given: POST /api/articles with invalid title (empty)
Then: Response has status 400
And: Error code is VALIDATION_ERROR
And: Error details include field: "title"

Test: API Enforces Authentication

Given: No auth token
When: GET /api/articles (requires auth)
Then: Response has status 401
And: Error code is AUTH_REQUIRED
```

## Common API Mistakes

**Mistake 1: Inconsistent Status Codes**
Problem: 200 for everything, even errors
Fix: Use correct HTTP status codes

**Mistake 2: No Error Details**
Problem: "Error" with no context
Fix: Provide code, message, and field-level details

**Mistake 3: Breaking Changes Without Version**
Problem: API changes, client breaks
Fix: Use versioning, maintain backward compatibility

**Mistake 4: Unclear Field Types**
Problem: "id" could be UUID or integer
Fix: Document types explicitly

**Mistake 5: No Rate Limiting**
Problem: Client can hammer API
Fix: Implement rate limits

**Mistake 6: Passwords in Error Messages**
Problem: "Password is invalid" in logs
Fix: Never include passwords in errors or logs
