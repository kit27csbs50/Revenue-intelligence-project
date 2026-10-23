"""
Sample data loader for RevenueIQ.
Loads synthetic conversation data for demonstration purposes.

⚠️ IMPORTANT: This is clearly labeled SYNTHETIC SAMPLE DATA for demonstration only.
NOT real business data or findings.
"""
from services.database import Database
from services.analysis import ConversationAnalyzer
from services.routing import SmartRouter
from config import Config
from datetime import datetime, timedelta
import random

# Sample conversations with diverse scenarios
SAMPLE_CONVERSATIONS = [
    {
        'conversation_id': 'CALL-001',
        'customer_name': 'John Smith',
        'customer_phone': '+1-555-0101',
        'customer_email': 'john.smith@techcorp.com',
        'customer_company': 'TechCorp Industries',
        'employee_name': 'Sarah Johnson',
        'conversation_type': 'Call',
        'transcript': 'I am very interested in purchasing your premium package. The features look great and I would like to place an order as soon as possible. Can you send me a quote?',
        'days_ago': 1
    },
    {
        'conversation_id': 'CALL-002',
        'customer_name': 'Emily Rodriguez',
        'customer_phone': '+1-555-0102',
        'customer_email': 'emily.r@innovate.com',
        'customer_company': 'Innovate Solutions',
        'employee_name': 'Mike Chen',
        'conversation_type': 'Call',
        'transcript': 'We are experiencing a technical issue with the login system. It keeps showing an error message and our team cannot access the dashboard. This is urgent - we need help immediately.',
        'days_ago': 0
    },
    {
        'conversation_id': 'MEET-001',
        'customer_name': 'David Park',
        'customer_phone': '+1-555-0103',
        'customer_email': 'david.park@globaltech.com',
        'customer_company': 'Global Tech Ltd',
        'employee_name': 'Sarah Johnson',
        'conversation_type': 'Meeting',
        'transcript': 'Thank you for the excellent demonstration. We are very impressed with the platform capabilities. Our team is excited to move forward with implementation.',
        'days_ago': 2
    },
    {
        'conversation_id': 'CALL-003',
        'customer_name': 'Lisa Wang',
        'customer_phone': '+1-555-0104',
        'customer_email': 'lisa.wang@startupco.com',
        'customer_company': 'StartupCo',
        'conversation_type': 'Call',
        'transcript': 'I am disappointed with the service quality. We have been waiting for a response for three days and nobody has followed up. This is unacceptable for a premium service.',
        'days_ago': 1
    },
    {
        'conversation_id': 'CALL-004',
        'customer_name': 'Michael Brown',
        'customer_phone': '+1-555-0105',
        'customer_email': 'mbrown@enterprises.com',
        'customer_company': 'Enterprise Solutions',
        'employee_name': 'David Park',
        'conversation_type': 'Call',
        'transcript': 'Could you please provide pricing information for the enterprise plan? We are evaluating different vendors and would like to see a detailed quote including volume discounts.',
        'days_ago': 3
    },
    {
        'conversation_id': 'MEET-002',
        'customer_name': 'Jennifer Lee',
        'customer_phone': '+1-555-0106',
        'customer_email': 'jlee@acmecorp.com',
        'customer_company': 'Acme Corporation',
        'employee_name': 'Emily Rodriguez',
        'conversation_type': 'Meeting',
        'transcript': 'We would like to schedule a product demonstration for our team next week. Can you show us the analytics features and how they integrate with our existing systems?',
        'days_ago': 4
    },
    {
        'conversation_id': 'CALL-005',
        'customer_name': 'Robert Taylor',
        'customer_phone': '+1-555-0107',
        'customer_email': 'rtaylor@businessinc.com',
        'customer_company': 'Business Inc',
        'conversation_type': 'Call',
        'transcript': 'The software crashed during our presentation to the board. We lost important data and this is a critical problem. We need technical support right now.',
        'days_ago': 0
    },
    {
        'conversation_id': 'CALL-006',
        'customer_name': 'Amanda Martinez',
        'customer_phone': '+1-555-0108',
        'customer_email': 'amartinez@techventures.com',
        'customer_company': 'Tech Ventures',
        'employee_name': 'Sarah Johnson',
        'conversation_type': 'Call',
        'transcript': 'Thank you for the wonderful support. Your team has been fantastic in helping us get set up. We are very happy with the product and service.',
        'days_ago': 5
    },
    {
        'conversation_id': 'CALL-007',
        'customer_name': 'James Wilson',
        'customer_phone': '+1-555-0109',
        'customer_email': 'jwilson@digitalco.com',
        'customer_company': 'Digital Co',
        'conversation_type': 'Call',
        'transcript': 'Please follow up with me next week about the proposal. I need to discuss this with our procurement team before making a decision.',
        'days_ago': 6
    },
    {
        'conversation_id': 'MEET-003',
        'customer_name': 'Sarah Anderson',
        'customer_phone': '+1-555-0110',
        'customer_email': 'sanderson@megacorp.com',
        'customer_company': 'MegaCorp',
        'employee_name': 'Mike Chen',
        'conversation_type': 'Meeting',
        'transcript': 'Quarterly business review went well. Discussed expansion opportunities and additional features our team would like to see implemented.',
        'days_ago': 7
    },
    {
        'conversation_id': 'CALL-008',
        'customer_name': 'Christopher Davis',
        'customer_phone': '+1-555-0111',
        'customer_email': 'cdavis@retailcorp.com',
        'customer_company': 'Retail Corp',
        'conversation_type': 'Call',
        'transcript': 'How much does your basic plan cost? Also, do you offer any discounts for annual subscriptions or for startups?',
        'days_ago': 2
    },
    {
        'conversation_id': 'CALL-009',
        'customer_name': 'Michelle Thompson',
        'customer_phone': '+1-555-0112',
        'customer_email': 'mthompson@healthtech.com',
        'customer_company': 'HealthTech Inc',
        'employee_name': 'Lisa Wang',
        'conversation_type': 'Call',
        'transcript': 'We are ready to buy the professional package for our entire team of 50 users. Can you send us the contract documents today?',
        'days_ago': 1
    },
    {
        'conversation_id': 'CALL-010',
        'customer_name': 'Daniel Garcia',
        'customer_phone': '+1-555-0113',
        'customer_email': 'dgarcia@financegroup.com',
        'customer_company': 'Finance Group',
        'conversation_type': 'Call',
        'transcript': 'The export feature is not working properly. When I try to download reports, I get an error message. This is affecting our daily operations.',
        'days_ago': 3
    },
    {
        'conversation_id': 'MEET-004',
        'customer_name': 'Patricia Miller',
        'customer_phone': '+1-555-0114',
        'customer_email': 'pmiller@consultingfirm.com',
        'customer_company': 'Consulting Firm LLC',
        'employee_name': 'Emily Rodriguez',
        'conversation_type': 'Meeting',
        'transcript': 'Great meeting today. Would love to see a demo of the new features you mentioned. Can we schedule something for next month?',
        'days_ago': 8
    },
    {
        'conversation_id': 'CALL-011',
        'customer_name': 'Kevin Moore',
        'customer_phone': '+1-555-0115',
        'customer_email': 'kmoore@manufacturing.com',
        'customer_company': 'Manufacturing Co',
        'conversation_type': 'Call',
        'transcript': 'I called three days ago and still have not received a callback. Very frustrated with the lack of response. This is terrible customer service.',
        'days_ago': 4
    },
    {
        'conversation_id': 'CALL-012',
        'customer_name': 'Nancy White',
        'customer_phone': '+1-555-0116',
        'customer_email': 'nwhite@educationtech.com',
        'customer_company': 'Education Tech',
        'employee_name': 'David Park',
        'conversation_type': 'Call',
        'transcript': 'Interested in learning more about your platform. Could you send me some information about pricing and features?',
        'days_ago': 5
    },
    {
        'conversation_id': 'CALL-013',
        'customer_name': 'Steven Clark',
        'customer_phone': '+1-555-0117',
        'customer_email': 'sclark@logistics.com',
        'customer_company': 'Logistics Solutions',
        'conversation_type': 'Call',
        'transcript': 'We need immediate assistance. Our production system is down and we cannot process orders. This is an emergency situation that needs urgent attention.',
        'days_ago': 0
    },
    {
        'conversation_id': 'MEET-005',
        'customer_name': 'Betty Harris',
        'customer_phone': '+1-555-0118',
        'customer_email': 'bharris@marketingagency.com',
        'customer_company': 'Marketing Agency',
        'employee_name': 'Sarah Johnson',
        'conversation_type': 'Meeting',
        'transcript': 'Excellent presentation! Our team is very excited about the possibilities. Looking forward to working together on this project.',
        'days_ago': 9
    },
    {
        'conversation_id': 'CALL-014',
        'customer_name': 'Thomas Martinez',
        'customer_phone': '+1-555-0119',
        'customer_email': 'tmartinez@realestate.com',
        'customer_company': 'Real Estate Group',
        'conversation_type': 'Call',
        'transcript': 'What is the price difference between the standard and premium tiers? Also, can we get a deal if we sign a multi-year contract?',
        'days_ago': 6
    },
    {
        'conversation_id': 'CALL-015',
        'customer_name': 'Sandra Lopez',
        'customer_phone': '+1-555-0120',
        'customer_email': 'slopez@hospitality.com',
        'customer_company': 'Hospitality Services',
        'employee_name': 'Mike Chen',
        'conversation_type': 'Call',
        'transcript': 'Please call me back when you have a chance. I have some questions about the implementation timeline and training options.',
        'days_ago': 7
    },
    {
        'conversation_id': 'CALL-016',
        'customer_name': 'George Young',
        'customer_phone': '+1-555-0121',
        'customer_email': 'gyoung@construction.com',
        'customer_company': 'Construction Inc',
        'conversation_type': 'Call',
        'transcript': 'We want to purchase licenses for 100 employees. Can you provide a bulk pricing quote and help us with the onboarding process?',
        'days_ago': 2
    },
    {
        'conversation_id': 'CALL-017',
        'customer_name': 'Barbara King',
        'customer_phone': '+1-555-0122',
        'customer_email': 'bking@insurance.com',
        'customer_company': 'Insurance Services',
        'conversation_type': 'Call',
        'transcript': 'The mobile app keeps crashing when I try to upload files. This bug needs to be fixed as we rely on mobile access for field operations.',
        'days_ago': 1
    },
    {
        'conversation_id': 'MEET-006',
        'customer_name': 'Paul Wright',
        'customer_phone': '+1-555-0123',
        'customer_email': 'pwright@transportation.com',
        'customer_company': 'Transportation Co',
        'employee_name': 'Emily Rodriguez',
        'conversation_type': 'Meeting',
        'transcript': 'Very informative demo session. Would like to schedule a follow-up meeting to discuss custom integration requirements for our systems.',
        'days_ago': 10
    },
    {
        'conversation_id': 'CALL-018',
        'customer_name': 'Dorothy Scott',
        'customer_phone': '+1-555-0124',
        'customer_email': 'dscott@nonprofit.org',
        'customer_company': 'Nonprofit Organization',
        'conversation_type': 'Call',
        'transcript': 'Are there any special pricing programs available for nonprofit organizations? We are interested but working with a limited budget.',
        'days_ago': 8
    },
    {
        'conversation_id': 'CALL-019',
        'customer_name': 'Mark Green',
        'customer_phone': '+1-555-0125',
        'customer_email': 'mgreen@pharma.com',
        'customer_company': 'Pharma Solutions',
        'employee_name': 'Lisa Wang',
        'conversation_type': 'Call',
        'transcript': 'Absolutely love the new features you just released. The user interface improvements make everything so much easier. Great work!',
        'days_ago': 4
    },
    {
        'conversation_id': 'CALL-020',
        'customer_name': 'Carol Adams',
        'customer_phone': '+1-555-0126',
        'customer_email': 'cadams@automotive.com',
        'customer_company': 'Automotive Group',
        'conversation_type': 'Call',
        'transcript': 'The integration with our CRM is broken. Data is not syncing properly and we are seeing duplicate records. Need technical help urgently.',
        'days_ago': 1
    },
    {
        'conversation_id': 'CALL-021',
        'customer_name': 'Edward Baker',
        'customer_phone': '+1-555-0127',
        'customer_email': 'ebaker@energy.com',
        'customer_company': 'Energy Corporation',
        'conversation_type': 'Call',
        'transcript': 'Can you show me how the reporting module works? I would like to see a demonstration before we commit to the purchase.',
        'days_ago': 5
    },
    {
        'conversation_id': 'MEET-007',
        'customer_name': 'Helen Turner',
        'customer_phone': '+1-555-0128',
        'customer_email': 'hturner@telecommunications.com',
        'customer_company': 'Telecommunications Ltd',
        'employee_name': 'David Park',
        'conversation_type': 'Meeting',
        'transcript': 'Strategic planning session went very well. Discussed our expansion plans and how your platform can support our growth over the next three years.',
        'days_ago': 11
    },
    {
        'conversation_id': 'CALL-022',
        'customer_name': 'Andrew Phillips',
        'customer_phone': '+1-555-0129',
        'customer_email': 'aphillips@biotech.com',
        'customer_company': 'BioTech Innovations',
        'conversation_type': 'Call',
        'transcript': 'This is the worst experience I have ever had with a software company. Nothing works as advertised and support is non-existent. Extremely disappointed.',
        'days_ago': 3
    },
    {
        'conversation_id': 'CALL-023',
        'customer_name': 'Margaret Campbell',
        'customer_phone': '+1-555-0130',
        'customer_email': 'mcampbell@retailchain.com',
        'customer_company': 'Retail Chain',
        'employee_name': 'Sarah Johnson',
        'conversation_type': 'Call',
        'transcript': 'We are definitely interested in buying your solution. Can we schedule a call next week to finalize the details and sign the contract?',
        'days_ago': 2
    },
    {
        'conversation_id': 'CALL-024',
        'customer_name': 'Joshua Mitchell',
        'customer_phone': '+1-555-0131',
        'customer_email': 'jmitchell@aerospace.com',
        'customer_company': 'Aerospace Systems',
        'conversation_type': 'Call',
        'transcript': 'What are the costs for adding additional users to our existing account? Also, is there a discount for upgrading to the enterprise tier?',
        'days_ago': 6
    },
    {
        'conversation_id': 'CALL-025',
        'customer_name': 'Deborah Roberts',
        'customer_phone': '+1-555-0132',
        'customer_email': 'droberts@foodservice.com',
        'customer_company': 'Food Service Inc',
        'employee_name': 'Mike Chen',
        'conversation_type': 'Call',
        'transcript': 'Please get back to me when you can. I left a message yesterday about onboarding support and training schedules for our team.',
        'days_ago': 4
    },
    {
        'conversation_id': 'MEET-008',
        'customer_name': 'Ryan Carter',
        'customer_phone': '+1-555-0133',
        'customer_email': 'rcarter@architecture.com',
        'customer_company': 'Architecture Studio',
        'employee_name': 'Emily Rodriguez',
        'conversation_type': 'Meeting',
        'transcript': 'Fantastic demo! The design collaboration features are exactly what we need. Our architects will love this platform.',
        'days_ago': 12
    },
    {
        'conversation_id': 'CALL-026',
        'customer_name': 'Laura Perez',
        'customer_phone': '+1-555-0134',
        'customer_email': 'lperez@legalfirm.com',
        'customer_company': 'Legal Firm LLP',
        'conversation_type': 'Call',
        'transcript': 'The security certificate expired and now we cannot access the platform. This needs to be fixed immediately as we have urgent client work.',
        'days_ago': 0
    },
    {
        'conversation_id': 'CALL-027',
        'customer_name': 'Brian Evans',
        'customer_phone': '+1-555-0135',
        'customer_email': 'bevans@engineering.com',
        'customer_company': 'Engineering Solutions',
        'conversation_type': 'Call',
        'transcript': 'Just checking in to learn more about your services. Could you send me a brochure or product overview document?',
        'days_ago': 7
    },
    {
        'conversation_id': 'CALL-028',
        'customer_name': 'Nicole Rivera',
        'customer_phone': '+1-555-0136',
        'customer_email': 'nrivera@media.com',
        'customer_company': 'Media Productions',
        'employee_name': 'Lisa Wang',
        'conversation_type': 'Call',
        'transcript': 'Your support team is outstanding! They resolved our issue within an hour. Very impressed with the level of service and expertise.',
        'days_ago': 5
    },
    {
        'conversation_id': 'CALL-029',
        'customer_name': 'Eric Collins',
        'customer_phone': '+1-555-0137',
        'customer_email': 'ecollins@chemicals.com',
        'customer_company': 'Chemical Industries',
        'conversation_type': 'Call',
        'transcript': 'We need to place an order for 75 user licenses as soon as possible. Our team is ready to start using the system next week.',
        'days_ago': 1
    },
    {
        'conversation_id': 'MEET-009',
        'customer_name': 'Kimberly Stewart',
        'customer_phone': '+1-555-0138',
        'customer_email': 'kstewart@publishing.com',
        'customer_company': 'Publishing House',
        'employee_name': 'David Park',
        'conversation_type': 'Meeting',
        'transcript': 'Quarterly review meeting covered our content management needs. Discussed potential custom features for our editorial workflow.',
        'days_ago': 13
    },
    {
        'conversation_id': 'CALL-030',
        'customer_name': 'Jeffrey Morris',
        'customer_phone': '+1-555-0139',
        'customer_email': 'jmorris@utilities.com',
        'customer_company': 'Utilities Company',
        'conversation_type': 'Call',
        'transcript': 'The latest update introduced a bug that is preventing us from saving changes. This is blocking our work and needs urgent attention.',
        'days_ago': 2
    },
    {
        'conversation_id': 'CALL-031',
        'customer_name': 'Angela Murphy',
        'customer_phone': '+1-555-0140',
        'customer_email': 'amurphy@fashion.com',
        'customer_company': 'Fashion Retailers',
        'conversation_type': 'Call',
        'transcript': 'Could you provide pricing for both monthly and annual payment options? Also interested in learning about any current promotions.',
        'days_ago': 8
    },
    {
        'conversation_id': 'CALL-032',
        'customer_name': 'Justin Cook',
        'customer_phone': '+1-555-0141',
        'customer_email': 'jcook@gaming.com',
        'customer_company': 'Gaming Studios',
        'employee_name': 'Sarah Johnson',
        'conversation_type': 'Call',
        'transcript': 'Amazing product! The collaboration features have transformed how our team works together. Could not be happier with our decision.',
        'days_ago': 6
    },
    {
        'conversation_id': 'CALL-033',
        'customer_name': 'Rachel Rogers',
        'customer_phone': '+1-555-0142',
        'customer_email': 'rrogers@agriculture.com',
        'customer_company': 'Agriculture Corp',
        'conversation_type': 'Call',
        'transcript': 'I was promised a call back two weeks ago and never heard from anyone. This level of service is completely unacceptable.',
        'days_ago': 3
    },
    {
        'conversation_id': 'MEET-010',
        'customer_name': 'Aaron Reed',
        'customer_phone': '+1-555-0143',
        'customer_email': 'areed@security.com',
        'customer_company': 'Security Systems',
        'employee_name': 'Mike Chen',
        'conversation_type': 'Meeting',
        'transcript': 'Initial consultation meeting went great. Would like to schedule a technical deep-dive demo for our IT team next month.',
        'days_ago': 14
    },
    {
        'conversation_id': 'CALL-034',
        'customer_name': 'Melissa Bailey',
        'customer_phone': '+1-555-0144',
        'customer_email': 'mbailey@travel.com',
        'customer_company': 'Travel Agency',
        'conversation_type': 'Call',
        'transcript': 'Can we see a live demonstration of the customer relationship features? We are evaluating several platforms and want to compare functionality.',
        'days_ago': 4
    },
    {
        'conversation_id': 'CALL-035',
        'customer_name': 'Gregory Bell',
        'customer_phone': '+1-555-0145',
        'customer_email': 'gbell@sports.com',
        'customer_company': 'Sports Equipment',
        'employee_name': 'Emily Rodriguez',
        'conversation_type': 'Call',
        'transcript': 'Ready to move forward with the purchase. Please send the paperwork and we will get everything signed this week.',
        'days_ago': 1
    },
    {
        'conversation_id': 'CALL-036',
        'customer_name': 'Christine Cooper',
        'customer_phone': '+1-555-0146',
        'customer_email': 'ccooper@furniture.com',
        'customer_company': 'Furniture Designs',
        'conversation_type': 'Call',
        'transcript': 'We are experiencing slow performance issues during peak hours. The system becomes almost unusable. Please investigate and fix this problem.',
        'days_ago': 2
    },
    {
        'conversation_id': 'CALL-037',
        'customer_name': 'Brandon Richardson',
        'customer_phone': '+1-555-0147',
        'customer_email': 'brichardson@textiles.com',
        'customer_company': 'Textile Manufacturing',
        'conversation_type': 'Call',
        'transcript': 'Just following up on our previous conversation. Let me know when you have time to discuss the implementation plan.',
        'days_ago': 9
    },
    {
        'conversation_id': 'CALL-038',
        'customer_name': 'Samantha Cox',
        'customer_phone': '+1-555-0148',
        'customer_email': 'scox@cosmetics.com',
        'customer_company': 'Cosmetics Inc',
        'employee_name': 'Lisa Wang',
        'conversation_type': 'Call',
        'transcript': 'What is your best price for 50 users? We are comparing options and budget is a key factor in our decision.',
        'days_ago': 5
    },
    {
        'conversation_id': 'CALL-039',
        'customer_name': 'Tyler Howard',
        'customer_phone': '+1-555-0149',
        'customer_email': 'thoward@packaging.com',
        'customer_company': 'Packaging Solutions',
        'conversation_type': 'Call',
        'transcript': 'The onboarding process was smooth and the training materials are excellent. Very satisfied with how everything has been handled so far.',
        'days_ago': 7
    },
    {
        'conversation_id': 'CALL-040',
        'customer_name': 'Donna Ward',
        'customer_phone': '+1-555-0150',
        'customer_email': 'dward@pharmaceuticals.com',
        'customer_company': 'Pharmaceuticals Ltd',
        'conversation_type': 'Call',
        'transcript': 'Critical bug found - the data validation is failing and allowing incorrect entries. This could cause serious compliance issues for us.',
        'days_ago': 0
    },
    {
        'conversation_id': 'MEET-011',
        'customer_name': 'Jesse Torres',
        'customer_phone': '+1-555-0151',
        'customer_email': 'jtorres@aviation.com',
        'customer_company': 'Aviation Services',
        'employee_name': 'David Park',
        'conversation_type': 'Meeting',
        'transcript': 'Great partnership discussion. Looking forward to expanding our use of the platform across all our regional offices.',
        'days_ago': 15
    },
    {
        'conversation_id': 'CALL-041',
        'customer_name': 'Janet Peterson',
        'customer_phone': '+1-555-0152',
        'customer_email': 'jpeterson@beverages.com',
        'customer_company': 'Beverage Company',
        'conversation_type': 'Call',
        'transcript': 'Interested in purchasing but need more information first. Can you email me details about security certifications and compliance?',
        'days_ago': 6
    },
    {
        'conversation_id': 'CALL-042',
        'customer_name': 'Gerald Gray',
        'customer_phone': '+1-555-0153',
        'customer_email': 'ggray@mining.com',
        'customer_company': 'Mining Corporation',
        'employee_name': 'Sarah Johnson',
        'conversation_type': 'Call',
        'transcript': 'We want to order licenses for our entire organization - approximately 200 users. Can we discuss enterprise pricing and deployment support?',
        'days_ago': 2
    },
    {
        'conversation_id': 'CALL-043',
        'customer_name': 'Judith Ramirez',
        'customer_phone': '+1-555-0154',
        'customer_email': 'jramirez@dental.com',
        'customer_company': 'Dental Clinics',
        'conversation_type': 'Call',
        'transcript': 'Is there a discount available for healthcare providers? We operate multiple clinics and are looking for cost-effective solutions.',
        'days_ago': 8
    },
    {
        'conversation_id': 'CALL-044',
        'customer_name': 'Carl James',
        'customer_phone': '+1-555-0155',
        'customer_email': 'cjames@forestry.com',
        'customer_company': 'Forestry Management',
        'conversation_type': 'Call',
        'transcript': 'Please contact me to schedule a follow-up discussion. We have additional questions about the API integration capabilities.',
        'days_ago': 10
    },
    {
        'conversation_id': 'MEET-012',
        'customer_name': 'Gloria Watson',
        'customer_phone': '+1-555-0156',
        'customer_email': 'gwatson@financial.com',
        'customer_company': 'Financial Advisors',
        'employee_name': 'Mike Chen',
        'conversation_type': 'Meeting',
        'transcript': 'Excellent quarterly check-in. Reviewed our usage metrics and discussed opportunities for optimization and better ROI.',
        'days_ago': 16
    },
    {
        'conversation_id': 'CALL-045',
        'customer_name': 'Albert Brooks',
        'customer_phone': '+1-555-0157',
        'customer_email': 'abrooks@distribution.com',
        'customer_company': 'Distribution Networks',
        'conversation_type': 'Call',
        'transcript': 'The backup and recovery process failed last night. We lost several hours of work and need to understand what went wrong.',
        'days_ago': 1
    },
    {
        'conversation_id': 'CALL-046',
        'customer_name': 'Teresa Kelly',
        'customer_phone': '+1-555-0158',
        'customer_email': 'tkelly@veterinary.com',
        'customer_company': 'Veterinary Services',
        'employee_name': 'Emily Rodriguez',
        'conversation_type': 'Call',
        'transcript': 'Absolutely thrilled with the results! The platform has exceeded all our expectations. Thank you for the excellent product and support.',
        'days_ago': 4
    },
    {
        'conversation_id': 'CALL-047',
        'customer_name': 'Harold Sanders',
        'customer_phone': '+1-555-0159',
        'customer_email': 'hsanders@maritime.com',
        'customer_company': 'Maritime Shipping',
        'conversation_type': 'Call',
        'transcript': 'Can you show us a demo of the inventory tracking features? We need to see how it would work with our existing warehouse management system.',
        'days_ago': 5
    },
    {
        'conversation_id': 'CALL-048',
        'customer_name': 'Janice Price',
        'customer_phone': '+1-555-0160',
        'customer_email': 'jprice@wineries.com',
        'customer_company': 'Winery Group',
        'conversation_type': 'Call',
        'transcript': 'Please provide a quote for annual subscription with premium support. We are ready to buy if the pricing is competitive.',
        'days_ago': 3
    },
    {
        'conversation_id': 'CALL-049',
        'customer_name': 'Willie Bennett',
        'customer_phone': '+1-555-0161',
        'customer_email': 'wbennett@plastics.com',
        'customer_company': 'Plastics Manufacturing',
        'conversation_type': 'Call',
        'transcript': 'Horrible experience from start to finish. The product does not work as promised and customer support has been useless. Want a full refund.',
        'days_ago': 2
    },
    {
        'conversation_id': 'CALL-050',
        'customer_name': 'Diana Wood',
        'customer_phone': '+1-555-0162',
        'customer_email': 'dwood@recycling.com',
        'customer_company': 'Recycling Services',
        'employee_name': 'Lisa Wang',
        'conversation_type': 'Call',
        'transcript': 'We would like to purchase your solution. Please send us the contract and onboarding information so we can get started immediately.',
        'days_ago': 1
    }
]

def load_sample_data():
    """Load synthetic sample conversations into database."""
    print("Loading sample data into RevenueIQ...")
    print("⚠️  Note: This is SYNTHETIC SAMPLE DATA for demonstration only.\n")
    
    db = Database(Config.DATABASE_URL)
    analyzer = ConversationAnalyzer()
    router = SmartRouter()
    
    loaded_count = 0
    
    for conv in SAMPLE_CONVERSATIONS:
        try:
            # Calculate timestamp
            days_ago = conv.pop('days_ago', 0)
            timestamp = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d %H:%M:%S')
            
            # Analyze conversation
            analysis = analyzer.analyze_conversation(conv['transcript'])
            routing = router.route_conversation(analysis)
            
            # Prepare conversation data
            conversation_data = {
                'conversation_id': conv['conversation_id'],
                'customer_name': conv['customer_name'],
                'customer_phone': conv.get('customer_phone'),
                'customer_email': conv.get('customer_email'),
                'customer_company': conv.get('customer_company'),
                'employee_name': conv.get('employee_name'),
                'conversation_type': conv['conversation_type'],
                'timestamp': timestamp,
                'transcript': conv['transcript'],
                'summary': conv['transcript'][:100] + '...' if len(conv['transcript']) > 100 else conv['transcript'],
                'sentiment': analysis['sentiment'],
                'priority': routing['priority'],
                'status': 'Open',
                'assigned_team': routing['assigned_team'],
                'assigned_employee': conv.get('employee_name'),
                'next_action': routing['next_action'],
                'routing_reason': routing['routing_reason'],
                'follow_up_status': routing['follow_up_status'],
                'source': 'sample_data'
            }
            
            # Insert conversation
            if db.create_conversation(conversation_data):
                loaded_count += 1
                print(f"✓ Loaded: {conv['conversation_id']} - {conv['customer_name']}")
            else:
                print(f"✗ Skipped: {conv['conversation_id']} (already exists)")
        
        except Exception as e:
            print(f"✗ Error loading {conv.get('conversation_id', 'unknown')}: {e}")
    
    print(f"\n✓ Successfully loaded {loaded_count} sample conversations")
    print("\nNext step: Run 'python app.py' to start the application")

if __name__ == '__main__':
    load_sample_data()
