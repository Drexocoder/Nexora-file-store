# Nexora Bot Factory V2

## Product direction

Nexora Bot Factory is being rebuilt as a clean, fast Telegram bot-template platform. The previous File Store, Link Protect, and Cricket Tournament clone templates are archived and must not be offered by the new Factory UI.

New templates will be added through the template registry.

## Core principles

- Premium, minimal, aesthetic Telegram UI.
- Fast async deployment and low-latency interactions.
- Template-driven architecture instead of template-specific logic in the Factory.
- Telegram BotFather command menu is configured automatically from each template manifest.
- Bot command-menu configuration is separate from owner/admin controls.
- Platform economy is controlled by the Nexora main owner.
- Telegram Stars are NOT used for purchases.
- Coin purchases use manual UPI payment and main-owner approval.
- All wallet activity is auditable.
- Main-owner settings are configurable without code changes.

## Deployment

### Token flow

1. User submits a BotFather token.
2. Factory validates the token.
3. User selects an available template.
4. Factory checks template access/pricing.
5. Deployment starts.
6. Template is loaded.
7. Bot commands are registered with Telegram.
8. Bot description and short description are configured.
9. Bot starts.
10. User receives a compact LIVE confirmation.

### BotFather command menu

Every template owns a command manifest. Commands are pushed automatically to Telegram using the Bot API/Pyrogram command configuration.

Example commands:

- /start — Start the bot
- /play — Play
- /profile — My profile
- /leaderboard — Leaderboard
- /help — Help

This is the Telegram command menu for the deployed bot. It is NOT an owner command such as /commands.

## Template marketplace

Each template supports:

- Name
- Slug
- Description
- Category
- Icon/custom emoji
- Features
- Commands
- Version
- Status
- Deployment count
- Pricing mode
- Coin price
- Optional INR price
- Free/premium state
- Release/update metadata

Pricing modes may include:

- Free
- Nexora Coins
- Manual UPI
- Redeem-code unlock
- Referral/event unlock

The main owner controls availability and pricing.

## Nexora Coins

Platform currency: Nexora Coins.

Each Factory user has a wallet and immutable transaction history.

Wallet records should support:

- Current balance
- Total earned
- Total spent
- Transaction ID
- Type/source
- Amount
- Balance before
- Balance after
- Timestamp
- Related user/order/redeem/referral
- Admin/operator when manually adjusted

### Earning sources

Configurable by the main owner:

- Referrals
- Redeem codes
- Daily rewards
- Missions/events
- Promotional campaigns
- Manual admin rewards
- Other future reward sources

Example configurable rule: 1 qualified reward action = 2 coins.

The actual value must be stored in platform settings, not hardcoded.

## Buying coins

Telegram Stars are intentionally excluded from purchases.

Coins are purchased through manual UPI.

Flow:

1. User selects a coin package.
2. Factory shows UPI ID/payment instructions.
3. User pays manually.
4. User submits UTR/transaction reference.
5. Order enters pending state.
6. Main owner reviews the payment.
7. Owner approves or rejects.
8. Approved coins are credited exactly once.
9. Wallet ledger and main-owner log are updated.

Coin packages are fully configurable:

- Package name
- INR amount
- Coin amount
- Bonus coins
- Active/inactive
- Display order
- Purchase limits

## Referrals

Every user receives a unique referral link.

Referral rewards are paid only after a configurable qualification event. Merely opening /start must not automatically create a reward.

Main-owner controls:

- Referral system enabled/disabled
- Reward amount
- Qualification requirement
- Per-user limits
- Campaign windows
- Maximum rewards
- Leaderboard visibility

Possible qualification events:

- Complete onboarding
- Create first bot
- Deploy first bot
- Complete another owner-configured action

Referral records must prevent duplicate rewards and support auditing.

## Redeem codes

Main owner can create codes for:

- Coins
- Template unlocks
- Premium access
- Discounts
- Event rewards

Code settings:

- Code value
- Reward type
- Reward amount
- Usage limit
- Per-user limit
- Start time
- Expiry
- Enabled/disabled
- Campaign/notes

Every redemption is logged and must be idempotent.

## Main-owner control plane

The main owner manages the entire platform economy and catalog.

### Users

- Search
- View wallet
- View transactions
- View referrals
- View deployed bots
- Block/unblock
- Manual coin adjustment with reason

### Bots

- Search/list
- Health/status
- Owner
- Template
- Version
- Users/deployments
- Logs
- Restart/disable
- Update

### Templates

- Add/edit
- Publish/unpublish
- Free/premium
- Pricing
- Commands
- Versioning
- Feature metadata
- Deployment limits
- Update/release management

### Economy

- Coin packages
- UPI settings
- Referral rewards
- Qualification rules
- Daily rewards
- Mission/event rewards
- Spending prices
- Global economy switches

### Payments

- Pending
- Approved
- Rejected
- UTR
- Amount
- Coins
- User
- Order ID
- Audit history

### Redeem

- Create
- Bulk generate
- Expiry
- Usage limits
- Disable
- View redemption history

### Broadcast

- All Factory users
- Bot owners
- Future segmented audiences

## Logging

Three distinct logging layers:

### 1. Clone bot admin log

Per deployed bot. Visible to that bot's owner/admin.

Examples:

- New user
- User action
- Bot-specific event
- Owner setting change
- Broadcast
- Bot-specific errors

### 2. Nexora main-owner activity log

Platform-level events:

- Deployment
- Payment approval/rejection
- Coin purchase
- Coin adjustment
- Referral qualification
- Redeem
- Template changes
- User actions
- Bot lifecycle events

### 3. System/developer log

Internal operational events:

- Telegram API errors
- Database errors
- Deployment failures
- Worker failures
- Payment failures
- Unexpected exceptions

## UI

The new UI should be compact and aesthetic:

- Short headers
- Clear hierarchy
- Minimal text
- Consistent button layouts
- Primary/secondary/danger navigation
- Pagination for large lists
- Edit existing messages where practical
- Avoid unnecessary message spam
- Use the Nexora premium custom emoji registry consistently

## Performance

Target a fast deployment and interaction path using:

- Async database operations
- Connection pooling
- Cached template manifests
- Indexed database queries
- Background workers for long-running operations
- Parallel independent deployment configuration
- Idempotent payment/reward operations
- Minimal Telegram API calls
- No unnecessary full-table loads

## Architecture

Suggested boundaries:

    app/
      factory/
      owner/
      admin/
      users/

    bot/
      deployment/
      botfather/
      commands/
      runtime/

    templates/
      registry/
      manifests/

    billing/
      wallet/
      coins/
      payments/
      referrals/
      redeem/

    logging/
      bot_admin/
      factory/
      system/

    core/
      emojis.py
      permissions.py
      cache.py
      config.py

    database/
    workers/

## Migration rule

The old clone implementations remain archived during the rebuild. They must not be exposed through the new template marketplace.

New templates should be added through manifests/registry rather than adding another large special-case handler to the Factory.
