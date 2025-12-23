# Technical Design Document (TDD) Template & Guide

A well-structured Technical Design Document is the blueprint for engineering teams. It translates product vision and design into concrete implementation guidance.

## TDD Structure

### 1. Executive Summary (1-2 pages)

**Purpose**: Give readers a quick understanding of the design without reading 30 pages.

**Include**:
- **Business Context**: Why are we building this? What problem does it solve?
- **Goals**: What are we trying to achieve? Success metrics?
- **Approach**: High-level technical strategy (1-3 paragraphs)
- **Timeline**: Rough phases and duration
- **Key Risks**: Most critical technical risks

**Example**:
```
We're building a favorites feature to increase engagement and content discovery.
Users will be able to save articles, projects, and other content for quick access.

Technical Approach:
- Simple client-side bookmarking with server sync
- Backend stores favorites in user's profile
- Real-time sync across user's devices via WebSocket
- Graceful degradation if sync fails (queued locally)

Timeline: 6 weeks
- Phase 1 (2 weeks): Core favorite/unfavorite endpoints
- Phase 2 (2 weeks): Real-time sync with WebSocket
- Phase 3 (2 weeks): Offline support and queue system

Key Risks:
- Real-time sync scale (handling thousands of concurrent clients)
- Conflict resolution when user edits offline then comes online
- Testing real-time scenarios in CI/CD
```

### 2. Architecture Overview (2-3 pages)

**Purpose**: Help readers understand the system at a high level.

**Include**:
- **System Diagram**: Components and how they connect
- **Data Flow**: How data moves through the system
- **Technology Stack**: Languages, frameworks, databases, infrastructure

**System Diagram Example**:
```
┌─────────────────────────────────────────────┐
│             Client (Web/Mobile)             │
│ ┌─────────────────────────────────────────┐ │
│ │   UI Components                         │ │
│ │   ┌──────────────┐  ┌──────────────┐   │ │
│ │   │ Favorites    │  │ Local State  │   │ │
│ │   │ Button/View  │  │ (Redux)      │   │ │
│ │   └──────────────┘  └──────────────┘   │ │
│ └─────────────────────────────────────────┘ │
│              ▲                     ▲         │
│              │ HTTP/JSON           │ WS      │
└──────────────┼─────────────────────┼─────────┘
               │                     │
        ┌──────▼──────────────────────▼──────┐
        │      API Gateway / Load Balancer   │
        └──────┬──────────────────────┬──────┘
               │                      │
        ┌──────▼────────┐      ┌──────▼──────────┐
        │ REST API      │      │ WebSocket       │
        │ - Get favs    │      │ - Real-time     │
        │ - Add/remove  │      │   sync          │
        │ - Paginate    │      │ - Reconnect     │
        └──────┬────────┘      └──────┬──────────┘
               │                      │
        ┌──────▼──────────────────────▼──────┐
        │   Backend Service Layer             │
        │   - Favorites business logic        │
        │   - Authorization checks           │
        │   - Event publishing               │
        └──────┬──────────────────────┬──────┘
               │                      │
        ┌──────▼─────────┐   ┌────────▼────────┐
        │ PostgreSQL      │   │ Redis (Cache)   │
        │ - Favorites     │   │ - User favorites│
        │ - User profile  │   │ - Sessions      │
        └─────────────────┘   └─────────────────┘
```

**Data Flow Example**:
```
Happy Path: User saves an article
1. Frontend: User clicks "Save" button
2. Frontend: Immediately adds to UI (optimistic update)
3. Frontend: Sends HTTP POST /users/{id}/favorites
4. Backend: Validates user authorization
5. Backend: Inserts favorite into database
6. Backend: Publishes "FavoritesChanged" event
7. Backend: Returns 201 Created
8. Frontend: Confirms save succeeded, updates UI state
9. WebSocket: Propagates change to user's other devices

Failure Path: Network timeout
1-3. Same as above
4. Backend: Connection times out (no response)
5. Frontend: After 3s timeout, shows error toast
6. Frontend: Saves action to local queue (IndexedDB)
7. Frontend: Shows "Will sync when online"
8. User comes online: Frontend processes queue
9. Same as steps 4-9 above
```

**Technology Stack Example**:
```
Frontend:
- React 18 with TypeScript
- Redux for state management
- Socket.io-client for WebSocket
- Tailwind CSS for styling
- Vite for build

Backend:
- Node.js 18 with Express
- Socket.io for WebSocket
- PostgreSQL 14 for persistence
- Redis for caching and sessions
- TypeScript for type safety

Infrastructure:
- AWS EC2 for application servers
- RDS for PostgreSQL
- ElastiCache for Redis
- CloudFront for CDN
- CloudWatch for monitoring
```

### 3. Data Models (2-3 pages)

**Purpose**: Define the structure of data in the system.

**For Each Entity**:
- **Name**: What is it?
- **Fields**: What data does it contain?
- **Types & Constraints**: Types, required, ranges, formats
- **Relationships**: How does it relate to other entities?
- **Lifecycle**: How is it created, updated, deleted?

**Example**:
```
Entity: Favorite
Description: A user's bookmarked content item

Fields:
- id (UUID, primary key)
  Required: Yes
  Immutable: Yes
  
- user_id (UUID, foreign key)
  Required: Yes
  Immutable: Yes
  Reference: User.id
  Cascade: DELETE (if user deleted, favorite deleted)
  
- item_id (UUID, foreign key)
  Required: Yes
  Immutable: Yes
  Reference: Item.id
  Cascade: SET NULL (if item deleted, favorite kept but item_id nulled)
  
- item_type (Enum: 'article', 'project', 'video')
  Required: Yes
  Immutable: Yes
  
- created_at (Timestamp)
  Required: Yes
  Immutable: Yes
  Default: Now()
  
- updated_at (Timestamp)
  Required: Yes
  Immutable: No
  Default: Now()
  Updated: On any field change

Relationships:
- Belongs to: User (many favorites per user)
- References: Item (polymorphic—article, project, or video)

Constraints:
- Unique: (user_id, item_id, item_type)
  Prevents duplicate favorites of same item
  
Lifecycle:
- Created: When user clicks "Save"
- Updated: Never updated in practice (immutable except updated_at)
- Deleted: When user clicks "Remove" or item is deleted

Queries:
- Get all favorites for user (paginated, ordered by created_at DESC)
- Get specific favorite (check user owns it)
- Check if item is favorited (fast, optimized for UI)
- Count favorites per item (for popularity metrics)

Indices:
- PRIMARY KEY (id)
- UNIQUE (user_id, item_id, item_type)
- INDEX (user_id, created_at DESC) - for listing
- INDEX (item_id, item_type) - for cascade deletes
```

### 4. System Components (3-4 pages)

**Purpose**: Define the major pieces and how they fit together.

**Frontend Component Example**:
```
State Management (Redux)

Store Structure:
favorites: {
  byId: {
    "item-123": {
      id: "item-123",
      itemId: "article-456",
      itemType: "article",
      createdAt: "2024-12-20T10:00:00Z"
    }
  },
  allIds: ["item-123", "item-124"],
  loading: false,
  error: null,
  syncQueue: [
    { action: "add", itemId: "article-789", itemType: "article" }
  ],
  isOnline: true
}

Actions:
- ADD_TO_FAVORITES
  Payload: { itemId, itemType }
  Optimistic: Yes (add to state immediately)
  Queue: Yes (if offline, add to syncQueue)
  
- REMOVE_FROM_FAVORITES
  Payload: { id }
  Optimistic: Yes
  Queue: Yes
  
- SYNC_FAVORITES (periodic)
  Reconcile local state with server
  
- SET_ONLINE_STATUS
  Whether network is available
  Trigger queue processing when online

Selectors:
- isFavorited(itemId, itemType): boolean
- getAllFavorites(): Favorite[]
- getFavoritesLoading(): boolean
- getFavoritesError(): string | null
- getSyncQueueSize(): number
```

**Backend Service Example**:
```
Favorites Service

Core Methods:

1. addFavorite(userId, itemId, itemType, sourceIp)
   Input:
   - userId: UUID (from auth token)
   - itemId: UUID (item being favorited)
   - itemType: 'article' | 'project' | 'video'
   - sourceIp: string (for audit logging)
   
   Process:
   - Validate user_id belongs to auth token
   - Validate item exists and belongs to itemType
   - Check rate limit (max 100 favorites per hour)
   - Insert into Favorites table
   - Publish 'FAVORITE_ADDED' event
   - Invalidate cache
   - Return created favorite
   
   Error Cases:
   - 401: Invalid auth token
   - 403: Unauthorized (token user != userId)
   - 404: Item not found
   - 409: Already favorited
   - 429: Rate limit exceeded
   - 500: Database error
   
2. removeFavorite(userId, favoriteId)
   Same validation and caching
   
3. getFavorites(userId, limit, offset)
   Input:
   - userId: UUID
   - limit: 1-100 (default 20)
   - offset: 0-1000
   
   Process:
   - Validate user_id
   - Check cache first (1 hour TTL)
   - Query database with indices
   - Enrich with item details
   - Update cache
   - Return paginated results
   
   Performance:
   - < 200ms target (cached)
   - < 500ms target (uncached)

4. isFavorited(userId, itemId, itemType)
   Special optimized query
   - Single DB lookup
   - < 50ms target
   - Used frequently by UI
```

### 5. API & Contract Specifications (3-4 pages)

**Purpose**: Define the interface between frontend and backend.

**Example REST API**:
```
GET /api/users/{userId}/favorites
Purpose: Get user's favorited items

Auth: Required (Bearer token, user owns {userId})

Query Parameters:
- limit: integer, 1-100, default 20
- offset: integer, >= 0, default 0
- type: string, 'article'|'project'|'video', optional (filter by type)
- sort: string, 'newest'|'oldest'|'title', default 'newest'

Response: 200 OK
{
  "data": [
    {
      "id": "fav-123",
      "itemId": "article-456",
      "itemType": "article",
      "item": {
        "id": "article-456",
        "title": "Understanding APIs",
        "thumbnail": "https://...",
        "author": "Jane Smith"
      },
      "createdAt": "2024-12-20T10:00:00Z"
    }
  ],
  "pagination": {
    "offset": 0,
    "limit": 20,
    "total": 45,
    "hasMore": true
  }
}

Errors:
401 Unauthorized
{
  "error": {
    "code": "AUTH_REQUIRED",
    "message": "Authentication token required"
  }
}

403 Forbidden
{
  "error": {
    "code": "FORBIDDEN",
    "message": "Cannot access other user's favorites"
  }
}

429 Too Many Requests
{
  "error": {
    "code": "RATE_LIMIT",
    "message": "Too many requests. Retry after 60 seconds",
    "retryAfter": 60
  }
}

---

POST /api/users/{userId}/favorites
Purpose: Add item to favorites

Auth: Required

Body:
{
  "itemId": "article-456",
  "itemType": "article"
}

Response: 201 Created
{
  "data": {
    "id": "fav-789",
    "itemId": "article-456",
    "itemType": "article",
    "createdAt": "2024-12-20T10:30:00Z"
  }
}

Errors:
400 Bad Request (missing fields, invalid itemType)
404 Not Found (item doesn't exist)
409 Conflict (already favorited)
429 Too Many Requests

---

DELETE /api/users/{userId}/favorites/{favoriteId}
Purpose: Remove from favorites

Auth: Required

Response: 204 No Content

Errors:
404 Not Found (favorite doesn't exist)
403 Forbidden (doesn't belong to user)
```

**WebSocket Events** (if applicable):
```
Connection:
Event: CONNECT
Message: {
  "type": "CONNECT",
  "userId": "user-123"
}
Response: { "status": "CONNECTED", "userId": "user-123" }

Sync Event:
Event: FAVORITES_CHANGED
Sent by backend when another client modifies favorites
Message: {
  "type": "FAVORITES_CHANGED",
  "action": "added" | "removed",
  "favoriteId": "fav-123",
  "itemId": "article-456",
  "itemType": "article",
  "timestamp": "2024-12-20T10:30:00Z"
}

Disconnect:
Event: DISCONNECT
Message: { "type": "DISCONNECT" }
Response: Connection closed

Reconnect:
- Automatic reconnect with exponential backoff
- After reconnect, client requests full sync
- Server sends any changes missed during disconnect
```

### 6. Implementation Phases (3-4 pages)

**Purpose**: Break implementation into manageable chunks.

**Phase Structure**:
```
PHASE 1: MVP - Core Favorites (2 weeks)

Scope:
✓ Add/remove favorite endpoints
✓ Basic frontend UI
✓ User can see their favorites
✓ Database schema and migrations
✗ Real-time sync (defer to Phase 2)
✗ Offline support (defer to Phase 3)

Success Criteria:
- User can favorite/unfavorite content
- Favorites list can be viewed
- Load test: 1000 concurrent users
- API response time < 500ms
- 95% uptime in staging

Technical Decisions:
- Single REST API (no WebSocket yet)
- PostgreSQL for persistence
- Redis for caching user's favorites
- No complex offline scenarios yet

Responsibilities:
Frontend:
- Favorite button component (loading, disabled, error states)
- Favorites list view with pagination
- Error handling and user messaging
- Integration with Redux store

Backend:
- Favorites endpoints (POST, DELETE, GET)
- Database schema and migrations
- Rate limiting (100 requests per hour per user)
- Basic error handling and validation
- Cache invalidation

Infrastructure:
- Database provisioning
- Cache provisioning
- Monitoring setup
- Log aggregation

Dependencies:
- Item service must provide item lookup endpoint
- User service must provide user info
- Auth service must validate tokens

Timeline: 2 weeks
- Week 1: Backend API, database, infrastructure
- Week 2: Frontend implementation, integration testing

Risks:
- Database query performance at scale
- Mitigation: Use indices, load test early

---

PHASE 2: Real-Time Sync (2 weeks)

Builds on Phase 1. Adds:
✓ WebSocket connection for real-time sync
✓ Sync across user's devices
✗ Conflict resolution (simple last-write-wins for now)
✗ Offline support (Phase 3)

Success Criteria:
- Multiple clients see changes < 2 seconds
- 100+ concurrent WebSocket connections
- 99% message delivery (within session)
- Graceful handling of connection drops

Technical Decisions:
- Socket.io for WebSocket (built-in fallbacks)
- Redis Pub/Sub for inter-server communication
- No explicit conflict resolution (client-side last-write-wins)

Responsibilities:
Backend:
- WebSocket server (Socket.io)
- Event publishing (FAVORITES_CHANGED)
- Subscription management
- Reconnection handling

Frontend:
- WebSocket client setup
- Listen for FAVORITES_CHANGED events
- Sync state with received events
- Reconnection UI (show "syncing...")

Infrastructure:
- WebSocket load balancing
- Redis Pub/Sub setup
- Monitoring for connection drops

Timeline: 2 weeks

Risks:
- WebSocket connection management at scale
- Message ordering issues
- Mitigation: Load test, monitor connection health

---

PHASE 3: Offline Support (2 weeks)

Builds on Phases 1-2. Adds:
✓ Local queue for offline favorites
✓ Automatic sync when online
✓ Conflict detection and resolution
✗ Offline search (defer)

Success Criteria:
- Favorites work offline
- Sync queue processes correctly
- Conflicts detected and handled
- No lost data (even if force-quit during offline state)

Technical Decisions:
- IndexedDB for local queue persistence
- Last-write-wins conflict resolution
- Exponential backoff for failed syncs

Responsibilities:
Backend:
- Version numbers on entities for conflict detection
- Conflict resolution logic

Frontend:
- IndexedDB queue management
- Queue processing (batched, with backoff)
- Conflict UI (show "conflicted - which version?")
- Service worker for offline detection

Timeline: 2 weeks
```

### 7. Happy Path & Failure Modes (4-5 pages)

**Purpose**: Document system behavior in all scenarios.

**Example: Save Favorite - Happy Path**:
```
SCENARIO: User saves an article to favorites

Preconditions:
- User is authenticated
- Article exists and is not already favorited
- Network is online
- Rate limit not exceeded

Steps:

1. USER ACTION
   - User clicks "Save" button on article

2. FRONTEND IMMEDIATE RESPONSE
   - Button shows loading state (spinner)
   - Button disabled to prevent double-click
   - Optimistically add favorite to Redux store
   - Update UI (button now shows "Saved")
   
3. FRONTEND NETWORK REQUEST
   - POST /api/users/{userId}/favorites
   - Body: { itemId: "...", itemType: "article" }
   - Headers: Authorization: Bearer {token}
   - Timeout: 3 seconds

4. BACKEND PROCESSING
   - Validate auth token
   - Validate user_id matches token
   - Validate item exists
   - Validate not already favorited
   - Check rate limit
   - Insert into favorites table
   - Invalidate user's favorites cache
   - Publish FAVORITE_ADDED event to Redis
   - Return 201 Created with favorite object

5. WEBSOCKET NOTIFICATION (Phase 2+)
   - Backend publishes FAVORITES_CHANGED event
   - All user's devices receive notification
   - Each device's Redux store updates

6. FRONTEND SUCCESS
   - Response 201 received
   - Button shows "Saved" state
   - Button enabled
   - Optional: Show success toast "Added to favorites"
   - Update Redux store with server version (for consistency)

RESULT: User's favorite saved, synced across devices

Timing:
- Button feedback: Instant (optimistic)
- Network round-trip: Typically 100-300ms
- Cross-device sync: Within 2 seconds (via WebSocket)
```

**Example: Save Favorite - Network Timeout**:
```
SCENARIO: Network is slow or unreliable

Preconditions:
- Same as happy path
- Network latency > 3 seconds OR connection lost

Steps:

1-2. Same as happy path (button shows loading, optimistic update)

3. FRONTEND NETWORK REQUEST
   - POST sent, but no response
   - 3 seconds pass (timeout threshold)

4. FRONTEND TIMEOUT HANDLING
   - Network request fails
   - If offline: Add to IndexedDB sync queue (Phase 3+)
   - Show error toast: "Couldn't save. Will retry when online."
   - Button returns to "Save" state (not saved state)
   - Redux store reverts optimistic update

5. USER RECOVERY PATHS
   
   a. Network comes back:
   - Frontend retries queued action
   - Same as happy path from step 3 onward
   - Show confirmation "Now saved" when complete
   
   b. User retries manually:
   - Clicks "Save" again
   - Same as happy path
   
   c. User gives up and leaves:
   - If Phase 3+ offline support: Action queued, will sync later
   - If Phase 1-2: Favorite not saved (user needs to retry)

RESULT: Favorite not saved, but user informed and can recover
```

**Example: Save Favorite - Already Favorited**:
```
SCENARIO: User tries to favorite same item twice

Preconditions:
- Item is already favorited by this user
- Unique constraint (user_id, item_id, item_type) prevents duplicates

Steps:

1-3. Same as happy path

4. BACKEND PROCESSING
   - All validation passes
   - INSERT fails: Unique constraint violation
   - Database returns error
   - Backend catches error
   - Detects it's a duplicate, not a real error

5. BACKEND RESPONSE
   - Return 409 Conflict
   - Body: 
   {
     "error": {
       "code": "ALREADY_FAVORITED",
       "message": "This item is already in your favorites"
     }
   }

6. FRONTEND ERROR HANDLING
   - 409 response received
   - Revert optimistic update (remove from Redux)
   - Show error toast: "Already in your favorites"
   - Optionally: Show button as "Saved" (since it is)

RESULT: Duplicate prevented, user informed
```

### 8. Non-Functional Requirements (2-3 pages)

**Purpose**: Define performance, scalability, security, reliability targets.

**Example**:
```
PERFORMANCE TARGETS

API Endpoints:
- GET /users/{id}/favorites: < 200ms (50th percentile, cached)
- GET /users/{id}/favorites: < 500ms (95th percentile, cached)
- POST /users/{id}/favorites: < 300ms
- DELETE /users/{id}/favorites/{id}: < 200ms

Database Query Performance:
- Favorite lookup (user_id, item_id): < 50ms
- List favorites (paginated): < 100ms

WebSocket Messaging:
- Event delivery latency: < 2 seconds
- Message throughput: 100+ concurrent users

Frontend Performance:
- Button click to loading state: Instant (< 16ms)
- List render: < 500ms for initial load

SCALING TARGETS

Concurrent Users:
- Phase 1-2: 10,000 concurrent users
- Phase 3+: 100,000 concurrent users

Data Volume:
- 1 million users
- Average 50 favorites per user
- 50 million total favorites
- Growth: 20% year-over-year

Scaling Strategy:
- Database: Horizontal partitioning by user_id (shard)
- Cache: Redis cluster with consistent hashing
- API Servers: Horizontal scaling with load balancer
- WebSocket: Redis Pub/Sub for inter-server communication

SECURITY

Authentication:
- OAuth 2.0 with JWT tokens
- Token expiration: 1 hour
- Refresh tokens: 30 days

Authorization:
- Users can only view/modify their own favorites
- Backend validates ownership on every operation

Data Protection:
- Favorites data in transit: HTTPS/TLS 1.2+
- Sensitive user data encrypted at rest (optional)
- No sensitive data in logs

Rate Limiting:
- 100 requests per hour per user (POST/DELETE)
- 1000 requests per hour per user (GET)
- IP-based fallback if rate-limited

Audit Logging:
- Log all favorite add/remove operations
- Retention: 90 days
- Fields logged: userId, itemId, timestamp, action, sourceIp

RELIABILITY

Uptime Target:
- Phase 1-2: 99% uptime (9.6 hours/month allowed downtime)
- Phase 3+: 99.9% uptime (43 minutes/month)

Disaster Recovery:
- Database backups: Daily, 30-day retention
- RTO (Recovery Time Objective): 1 hour
- RPO (Recovery Point Objective): 1 day

Graceful Degradation:
- If cache is down: Hit database directly (slower)
- If WebSocket is down: Client polls instead
- If favorites service is down: Can't add/remove, but UI stays responsive

Monitoring:
- Alert if API response time > 500ms
- Alert if WebSocket connections < 90% of expected
- Alert if error rate > 1%
- Monitor database replication lag
```

## TDD Quality Checklist

Before considering a TDD complete:

**Completeness**
- [ ] All system components defined?
- [ ] All API contracts specified?
- [ ] All data models documented?
- [ ] Happy path and failure scenarios covered?
- [ ] Non-functional requirements specified?
- [ ] Integration points with other systems clear?

**Clarity**
- [ ] A new engineer could start building from this?
- [ ] All terminology is consistent?
- [ ] Trade-offs are explained?
- [ ] Ambiguous sections have been resolved?
- [ ] Diagrams are clear and accurate?

**Feasibility**
- [ ] Is this buildable in estimated timeline?
- [ ] Are dependencies clear?
- [ ] Risks identified and mitigations planned?
- [ ] Do we have necessary infrastructure?

**Alignment**
- [ ] Does this match the product specification?
- [ ] Does this match the design specification?
- [ ] Have key stakeholders reviewed and agreed?
- [ ] Are there conflicting requirements surfaced?

## Common TDD Mistakes

**Mistake 1: Too Much Detail Too Early**
Problem: 50-page TDD before building anything
Fix: Start with 10-15 pages. Add detail as you build.

**Mistake 2: Missing Failure Scenarios**
Problem: Document happy path only
Fix: Document at least 3-5 failure scenarios per feature

**Mistake 3: Unclear Responsibility Boundaries**
Problem: It's not clear who builds what
Fix: For each component, explicitly assign frontend/backend/infra responsibility

**Mistake 4: No Trade-offs Section**
Problem: Design seems perfect but has hidden costs
Fix: Document trade-offs explicitly

**Mistake 5: Missing Integration Points**
Problem: Assume other systems work perfectly
Fix: Document what happens when other systems fail

**Mistake 6: Ignoring Offline/Degradation**
Problem: Design assumes network always works
Fix: Document offline behavior and graceful degradation

## TDD Review Checklist

When reviewing a TDD:

- [ ] Can you understand the design in 15 minutes?
- [ ] Are you clear on what each team builds?
- [ ] Do you see any missing scenarios?
- [ ] Are there trade-offs you'd reconsider?
- [ ] Do you see technical risks?
- [ ] Is the timeline realistic?
- [ ] Are there unclear API contracts?
- [ ] Would you implement differently? (If yes, discuss)

## TDD vs. Actual Implementation

A TDD is a blueprint, not a promise. Expect to:
- Discover things during implementation
- Hit unexpected technical challenges
- Need to adjust plans
- Learn and iterate

That's normal and healthy. A good TDD anticipates this and leaves room for learning.
