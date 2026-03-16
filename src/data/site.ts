/**
 * Site-wide configuration.
 *
 * Newsletter: change `provider` and `action` when you pick a platform.
 *
 * Buttondown:  action = "https://buttondown.com/api/emails/newsletter-subscribe"
 *              emailField = "email"
 *              Add: <input type="hidden" name="tag" value="blog" />
 *
 * Substack:    Link directly to your Substack subscribe page instead of embedding.
 *
 * ConvertKit:  action = "https://app.convertkit.com/forms/YOUR_FORM_ID/subscriptions"
 *              emailField = "email_address"
 */
export const newsletter = {
  /** Set to 'buttondown' | 'substack' | 'convertkit' | 'none */
  provider: "buttondown" as const,

  /** Form action URL. Update when you create an account. */
  action: "https://buttondown.com/api/emails/embed-subscribe/chiko",

  /** The name attribute for the email input. Varies by provider. */
  emailField: "email",
};
